from flask import(
    render_template,
    session,
    flash,
    redirect,
    url_for,
    request
)
from werkzeug.security import generate_password_hash, check_password_hash
from toy_tribe import app, db
from toy_tribe.models import Users, Toy, Profile, Review
from toy_tribe.forms import LoginForm, SignupForm, AddToy, EditToy

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/toys")
def toys():
    toys = list(Toy.query.order_by(Toy.name).all())
    # Get the user id to see if they created the toy in order to edit/delete
    user_id = session.get('user_id')
    return render_template("toys.html", toys = toys, user_id = user_id)

# Individual toy pages
@app.route('/toy/<int:toy_id>')
def individual_toy(toy_id):
    toy = Toy.query.get_or_404(toy_id)
    # Get the user id to see if they created the toy in order to edit/delete
    user_id = session.get('user_id')
    return render_template('individual_toy.html', toy=toy, user_id = user_id)


#Login form
@app.route('/login', methods=['GET', 'POST'])
def login():    
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Login successful', 'success')
            return render_template('home.html')
        else:
            flash('Login failed. Check your credentials.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('home'))

# Signup form
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
        new_user = Users(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

# Add toy form
@app.route('/add_toy', methods=['GET', 'POST'])
def add_toy():
    user_id = session.get('user_id')
    form = AddToy()
    # More comments
    if form.validate_on_submit():
        new_toy = Toy(user_id=user_id, name=form.name.data, company=form.company.data, type=form.type.data, is_approved=form.is_approved.data, image_url=form.image_url.data)
        db.session.add(new_toy)
        db.session.commit()
        return redirect(url_for('toys'))
    return render_template('add_toy.html', form = form)

# Edit toy form
@app.route('/edit_toy/<int:toy_id>', methods=['GET', 'POST'])
def edit_toy(toy_id):
    toy = Toy.query.get_or_404(toy_id)
    form = EditToy(obj=toy)
    ref = request.args.get('ref')
    if form.validate_on_submit():
        toy.name = form.name.data
        toy.company = form.company.data
        toy.type = form.type.data
        toy.is_approved = form.is_approved.data
        toy.image_url = form.image_url.data

        db.session.commit()
        if ref == 'toys':
            return redirect(url_for('toys'))
        else:
            return redirect(url_for('individual_toy', toy_id = toy.id))
    return render_template('edit_toy.html', form=form)

@app.route('/delete_toy/<int:toy_id>')
def delete_toy(toy_id):
    toy = Toy.query.get_or_404(toy_id)
    db.session.delete(toy)
    db.session.commit()
    return redirect(url_for('toys'))

# 404 error handling taken from:
@app.errorhandler(404)
def page_not_found(e):
    """
    Redirects to 404 page when the page is not found.

    """
    return render_template('404.html')