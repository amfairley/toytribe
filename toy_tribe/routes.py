from flask import render_template, session, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from toy_tribe import app, db
from toy_tribe.models import Users, Toy, Profile, Review
from toy_tribe.forms import LoginForm, SignupForm

@app.route("/")
def home():
    return render_template("base.html")

#Loginform

@app.route('/login', methods=['GET', 'POST'])
def login():    
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Login successful', 'success')
            return render_template('login.html', form=form)
        else:
            flash('Login failed. Check your credentials.', 'danger')
    return render_template('login.html', form=form)

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
