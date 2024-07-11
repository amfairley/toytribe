from flask import (
    render_template,
    session,
    flash,
    redirect,
    url_for,
    request
)
from werkzeug.security import generate_password_hash, check_password_hash
from toy_tribe import app, db
from toy_tribe.models import (
    Users,
    Toy,
    ToyType,
    Profile,
    Review
)
from toy_tribe.forms import (
    LoginForm,
    SignupForm,
    AddToy,
    EditToy
)


@app.route("/")
def home():
    """ A function that directs users to the homepage."""
    return render_template("home.html")


@app.route("/toys")
def toys():
    """
    A function that directs users to the toy page.
    Provides a list of toys in the Toy table allowing the page to display
    all of the toys.
    Provides the user_id of the logged in user in order to redirect
    logged out users to the homepage.
    """
    toys = list(Toy.query.order_by(Toy.name).all())
    # Display toy_types as a dictionary so I can get the value
    # assigned to the toy.toy_type_id
    toy_types = {toy_type.id: toy_type for toy_type in ToyType.query.all()}
    user_id = session.get('user_id')
    return render_template(
        "toys.html",
        toys=toys,
        user_id=user_id,
        toy_types=toy_types
    )


@app.route('/toy/<int:toy_id>')
def individual_toy(toy_id):
    """
    A function that directs users to individual toy pages.
    Provides a list of information for the specific toy to display to users.
    Provides the user_id of the logged in user in order to redirect
    logged out users to the homepage.
    """
    toy_types = {toy_type.id: toy_type for toy_type in ToyType.query.all()}
    toy = Toy.query.get_or_404(toy_id)
    user_id = session.get('user_id')
    return render_template(
        'individual_toy.html',
        toy=toy,
        user_id=user_id,
        toy_types=toy_types
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    A function that directs users to the login page.
    Utilizes the LoginForm form to get user data.
    Checks user data against the database and logs in if correct.
    Directs user to homepage on successful login.
    """
    form = LoginForm()
    # If there are no errors in the form when submitted:
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        # Checks that the user and password are correct
        # Directs user to home.html if correct
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            return render_template('home.html')
        # Displays a flash error if incorrect
        else:
            flash('Login failed. Check your credentials.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """
    A function that allows a user to log out 
    and redirects them to home.html.
    """
    session.pop('user_id', None)
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    A function that directs users to the signup page.
    Utilizes the SignupForm form to get user data.
    Creates a new entry in the Users table in the database.
    Redirects user to login page on successful signup.
    """
    form = SignupForm()
    # If there are no errors in the form when submitted:
    if form.validate_on_submit():
        # Creates a hashed password
        hashed_password = generate_password_hash(
            form.password.data,
            # Password-Based Key Derivation Function 2 (PBKDF2)
            # with the SHA-256 hash function.
            # For securely storing the password.
            method='pbkdf2:sha256',
            # 8 byte long random value to be added before the hashed password.
            salt_length=8
        )
        # New Users class instance with submitted data
        new_user = Users(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hashed_password
        )
        # Adds the new_user to the database and saves it
        db.session.add(new_user)
        db.session.commit()
        new_user_profile = Profile(
            user_id = new_user.id,
            about_me = "I am yet to fill this out.",
            user_image = "/static/img/default_toy.webp"
        )
        db.session.add(new_user_profile)
        db.session.commit()
        flash('Registration successful', 'success')
        # Redirects user to login page when signed up
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/add_toy', methods=['GET', 'POST'])
def add_toy():
    """
    A function that directs users to the add toy page.
    Utilizes the AddToy form to get user data.
    Creates a new entry in the Toy table in the database.
    Redirects user to toys page on successful addition of a new toy.
    """
    user_id = session.get('user_id')
    toy_types = ToyType.query.all()
    form = AddToy()
    form.toy_type_id.choices = [
        (toy_type.id, toy_type.toy_type) for toy_type in toy_types
    ]
    # If there are no errors in the form when submitted:
    if form.validate_on_submit():
        if not form.image_url.data:
            form.image_url.data = "/static/img/default_toy.webp"
        if not form.description.data:
            form.description.data = "No description added yet."
        # New Toy class instance with submitted data
        new_toy = Toy(
            user_id=user_id,
            name=form.name.data,
            company=form.company.data,
            toy_type_id=form.toy_type_id.data,
            description=form.description.data,
            image_url=form.image_url.data
        )
        # Adds the new_toy to the database and saves it
        db.session.add(new_toy)
        db.session.commit()
        # Redirects user back to toys when the new toy is added
        return redirect(url_for('toys'))
    return render_template('add_toy.html', form=form, toy_types=toy_types)


@app.route('/edit_toy/<int:toy_id>', methods=['GET', 'POST'])
def edit_toy(toy_id):
    """
    A function that directs users to the edit toy page.
    Utilizes the EditToy form to get user data.
    Updates the entry in the Toy table in the database with new data.
    Redirects user back to the page from which they accessed edit toy from.
    """
    toy = Toy.query.get_or_404(toy_id)
    form = EditToy(obj=toy)
    # Checks the reference of the a tag linking to edit_toy.html
    ref = request.args.get('ref')
    # Gets the type choices and gives them as options
    toy_types = ToyType.query.all()
    form.toy_type_id.choices = [
        (toy_type.id, toy_type.toy_type) for toy_type in toy_types
    ]
    # If there are no errors in the form when submitted:
    if form.validate_on_submit():
        # Sets values of Toy instance to new data
        toy.name = form.toy_type_id.data
        toy.company = form.company.data
        toy.toy_type_id = form.toy_type_id.data,
        toy.description = form.description.data
        toy.image_url = form.image_url.data
        # Saves these changes
        db.session.commit()
        # If the user came from toys, redirect back to toys
        if ref == 'toys':
            return redirect(url_for('toys'))
        # If the user came from individual_toy, redirect back there
        else:
            return redirect(url_for(
                'individual_toy',
                toy_id=toy.id,
                toy_types=toy_types
            ))
    return render_template(
        'edit_toy.html',
        form=form,
        toy_types=toy_types,
        toy=toy
    )


@app.route('/delete_toy/<int:toy_id>')
def delete_toy(toy_id):
    """A function used to remove the toy from Toy table in the database."""
    # Gets the correct toy
    toy = Toy.query.get_or_404(toy_id)
    # Deletes the toy
    db.session.delete(toy)
    db.session.commit()
    # Redirects back to toys.
    # No ref required: individual_toy would be deleted.
    return redirect(url_for('toys'))


@app.errorhandler(404)
def page_not_found(e):
    """Redirects to 404 page when the page is not found."""
    # Directs user and provides HTTP status code
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Redirects to a 500 page when there is an internal server error."""
    # Directs the user and provides HTTP status code
    return render_template('500.html'), 500
