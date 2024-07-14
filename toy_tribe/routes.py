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
    EditToy,
    EditProfile,
    AddReview,
    EditReview
)
import pycountry


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
    reviews = Review.query.filter_by(toy_id=toy.id).order_by(Review.id).all()
    return render_template(
        'individual_toy.html',
        toy=toy,
        user_id=user_id,
        toy_types=toy_types,
        reviews=reviews,
        Users=Users,
        Toy=Toy
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
            flash('Login failed. Check your credentials.')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """
    A function that allows a user to log out 
    and redirects them to home.html.
    """
    session.pop('user_id', None)
    # flash('You have been logged out successfully.', 'success')
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
        # Check if the email is already in use
        user=Users.query.filter_by(email=form.email.data).first()
        if user:
            flash('Email address already registered.')
        else:
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
                user_image = "/static/img/default_profile_image.webp"
            )
            db.session.add(new_user_profile)
            db.session.commit()
            # Redirects user to login page when signed up
            return redirect(url_for('login'))
    else:
        if form.errors:
            for field, errors, in form.errors.items():
                for error in errors:
                    flash(f"{field.capitalize()} error: {error}")
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
    form.toy_type_id.choices = [('0', "Select Toy Type")] + [
        (toy_type.id, toy_type.toy_type) for toy_type in toy_types
    ]
    # If there are no errors in the form when submitted:
    if form.is_submitted():
        if form.toy_type_id.data == 0:
            flash('Please select the toy type.')
        elif form.validate():
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

        # If statement to check toy_type is valid and throw error message
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

# Remove users define and return: used to put button to check links to other profiles work
@app.route('/profile')
def profile():
    """A function that directs users to their own profile page"""
    users = Users.query.all()
    # Get all countries
    country = pycountry.countries
    # Get the logged in user_id
    user_id = session.get("user_id")
    logged_in_user = session.get("user_id")
    # Get the user
    user = Users.query.get_or_404(user_id)
    user_profile = Profile.query.filter_by(user_id=user_id).first_or_404()
    # Set the flag_url correctly if chosen
    if user_profile.country:
        flag_url = "/static/img/flags/" + user_profile.country + ".svg"
    else:
        flag_url = None
    # Get user reviews
    reviews = Review.query.filter_by(user_id=user.id).order_by(Review.id).all()
    return render_template(
        'profile.html',
        user_id=user_id,
        user=user,
        user_profile=user_profile,
        users=users,
        flag_url = flag_url,
        logged_in_user=logged_in_user,
        reviews=reviews,
        # Get all toys to query for reviews
        Toy=Toy
    )


@app.route('/profile/<int:user_id>')
def other_profile(user_id):
    """A function that directs users to other users profile pages"""
    country = pycountry.countries
    logged_in_user = session.get("user_id")
    user = Users.query.get_or_404(user_id)
    user_profile = Profile.query.filter_by(user_id=user_id).first_or_404()    
    if user_profile.country:
        flag_url = "/static/img/flags/" + user_profile.country + ".svg"
    else:
        flag_url = None
    # Get user reviews
    reviews = Review.query.filter_by(user_id=user.id).order_by(Review.id).all()
    return render_template(
        'profile.html',
        user=user,
        user_profile=user_profile,
        logged_in_user=logged_in_user,
        flag_url=flag_url,
        reviews=reviews,
        # Get all toys to query for reviews
        Toy=Toy
    )

@app.route('/edit_profile/<int:user_id>', methods=['GET', 'POST'])
def edit_profile(user_id):
    """
    A function that directs users to the edit profile page.
    Utilizes the EditProfile form to get user data.
    Updates the entry in the Profile table in the database with new data.
    Redirects user back to the profile page.
    """
    user = Users.query.get_or_404(user_id)
    logged_in_user = session.get("user_id")
    profile = Profile.query.filter_by(user_id=user_id).first_or_404()
    # Get a list of countrys from pycountry library
    countries = sorted(pycountry.countries, key=lambda country: country.name)
    country_choices = [(country.alpha_2, country.name) for country in countries]
    # Sets the form and the country choices
    form = EditProfile(obj=profile)
    form.country.choices = country_choices
    # If there are no errors in the form when submitted:
    if form.validate_on_submit():
        profile.about_me = form.about_me.data
        profile.is_parent = form.is_parent.data
        profile.country = form.country.data
        profile.user_image = form.user_image.data
        # Saves these changes
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template(
        'edit_profile.html',
        profile=profile,
        form=form,
        countries=countries,
        user=user,
        logged_in_user=logged_in_user
    )


@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    """A function used to remove the user from Users table in the database."""
    # Gets the correct User
    user = Users.query.get_or_404(user_id)
    # Deletes the toy
    db.session.delete(user)
    db.session.commit()
    # Logs out
    session.pop('user_id', None)
    # Redirects back to home.
    return redirect(url_for('home'))

@app.route('/add_review/<int:toy_id>', methods=['GET', 'POST'])
def add_review(toy_id):
    """
    A function that directs users to the add review page.
    Utilizes the AddReview form to get user data.
    Creates a new entry in the Review table in the database
    Redirects user to individual toy page on successful addition of review.
    Redirects user back to the profile page.
    """
    # Get the toy that is being reviewed
    toy = Toy.query.get_or_404(toy_id)
    # Get the user doing the review
    user_id = session.get('user_id')
    # Get all toys and use it to populate the also_liked selection
    toys= Toy.query.all()
    toy_options = [(each_toy.id, each_toy.name) for each_toy in toys]
    # Set the form
    form = AddReview()
    # Set the also_liked selection choices
    form.also_liked.choices = toy_options
    # If there are no errors in the form when submitted:
    if form.is_submitted():
        if form.rating.data == '':
            flash('Please rate the toy.')
        elif form.validate():
            # New Review class instance with submitted data
            new_review = Review(
                user_id=user_id,
                toy_id=toy_id,
                review_content=form.review_content.data,
                rating=form.rating.data,
                also_liked = form.also_liked.data            
            )
            # Adds the new review to the database and saves it
            db.session.add(new_review)
            db.session.commit()
            # Redirects user back to toy when the review is added
            return redirect(url_for('individual_toy', toy_id=toy_id))
    return render_template('add_review.html', form=form, toy_id=toy_id, toy=toy)


@app.route('/edit_review/<int:review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    """
    A function that directs users to the edit review page.
    Utilizes the EditReview form to get user data.
    Updates the entry in the Review table in the database with new data.
    Redirects user back to the individual toy page.
    """
    # Get the review to be edited
    review = Review.query.get_or_404(review_id)
    # Get the toy that the review is for in order to redirect back to toy page
    toy = Toy.query.get_or_404(review.toy_id)
    toy_id = toy.id
    # Get the href ref for redirection:
    ref = request.args.get('ref')
    # Get all toys to populate the also_liked selection
    toys= Toy.query.all()
    toy_options = [(each_toy.id, each_toy.name) for each_toy in toys]
    # Select form to use and default values
    form = EditReview(
        review_content=review.review_content,
        rating = review.rating,
        also_liked = review.also_liked
    )
    # Set the also_liked selection choices
    form.also_liked.choices = toy_options
    # If there are no errors in the form when submitted:
    if form.validate_on_submit():
        review.review_content = form.review_content.data
        review.rating = form.rating.data
        review.also_liked = form.also_liked.data
        # Save the changes
        db.session.commit()
        # Redirect back to previous page
        if ref == 'toy':
            return redirect(url_for('individual_toy', toy_id=toy.id))
        else:
            return redirect(url_for('profile'))
    return render_template('edit_review.html', form=form, toy=toy)
    

@app.route('/delete_review/<int:review_id>')
def delete_review(review_id):
    """
    A function used to remove the review
    from Review table in the database.
    """
    # Gets the correct review
    review = Review.query.get_or_404(review_id)
    # Gets the toy id for redirection after deletion
    toy = Toy.query.get_or_404(review.toy_id)
    toy_id = toy.id    
    # Deletes the review
    db.session.delete(review)
    db.session.commit()
    # Redirects back to toy.
    return redirect(url_for('individual_toy', toy_id=toy_id))
