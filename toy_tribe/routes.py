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
    EditReview,
    ChangePassword
)
import pycountry
import re
from sqlalchemy import or_


@app.route("/")
def home():
    """ A function that directs users to the homepage."""
    return render_template("home.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    A function that directs users to the signup page.
    Utilizes the SignupForm form to get user data.
    Creates a new entry in the Users table in the database.
    Redirects user to login page on successful signup.
    """
    # Get the signup form
    form = SignupForm()
    # If there are no errors in the form when submitted:
    if form.validate_on_submit():
        # Check if the email is already in use
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            # Display error if the email is in use
            flash('Email address already registered.')
        else:
            # Creates a hashed password
            hashed_password = generate_password_hash(
                form.password.data,
                # Password-Based Key Derivation Function 2 (PBKDF2)
                # with the SHA-256 hash function.
                # For securely storing the password.
                method='pbkdf2:sha256',
                # 8 byte long random value to be added before
                # the hashed password.
                salt_length=8
            )
            # New Users class instance created with submitted data
            new_user = Users(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                username=form.username.data,
                email=form.email.data,
                password=hashed_password
            )
            # Adds the new_user to the database and saves it
            db.session.add(new_user)
            db.session.commit()
            # Creates a Profile class instance with the user data
            new_user_profile = Profile(
                user_id=new_user.id,
                about_me="I am yet to fill this out.",
                user_image="/static/img/default_profile_image.webp"
            )
            # Adds the profile to the database and saves it
            db.session.add(new_user_profile)
            db.session.commit()
            # Redirects user to login page when signed up
            return redirect(url_for('login'))
    else:
        # Display the errors
        for field, errors in form.errors.items():
            for error in errors:
                flash(error)
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    A function that directs users to the login page.
    Utilizes the LoginForm form to get user data.
    Checks user data against the database and logs in if correct.
    Directs user to homepage on successful login.
    """
    # Get the login form
    form = LoginForm()
    # If there are no errors in the form when submitted:
    if form.validate_on_submit():
        # Finds the user in the database by their email
        user = Users.query.filter_by(email=form.email.data).first()
        # Checks that the user and password are correct
        if user and check_password_hash(user.password, form.password.data):
            # Create a session with the logging in user
            session['user_id'] = user.id
            # Directs user to home.html
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
    # Remove the user from the current session and replace with None
    session.pop('user_id', None)
    # Redirect the user to the homepage
    return redirect(url_for('home'))


@app.route('/profile')
def profile():
    """A function that directs users to their own profile page"""
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
        flag_url = "/static/img/flags/" + user_profile.country.lower() + ".svg"
    else:
        flag_url = None
    # Get user reviews
    reviews = Review.query.filter_by(user_id=user.id).order_by(Review.id).all()
    # Get the sort options with default value
    sort_option = request.args.get('sort', 'newest_first')
    # Set sorting order
    if sort_option == 'newest_first':
        reviews = Review.query.filter_by(user_id=user.id).order_by(Review.id.desc()).all()
    elif sort_option == 'oldest_first':
        reviews = Review.query.filter_by(user_id=user.id).order_by(Review.id.asc()).all()         
    elif sort_option == 'rating_asc':
        reviews = Review.query.filter_by(user_id=user.id).order_by(Review.rating.asc()).all()
    elif sort_option == 'rating_desc':
        reviews = Review.query.filter_by(user_id=user.id).order_by(Review.rating.desc()).all()
    return render_template(
        'profile.html',
        user_id=user_id,
        logged_in_user=logged_in_user,
        user=user,
        user_profile=user_profile,
        flag_url=flag_url,
        reviews=reviews,
        sort_option=sort_option,
        # Get all toys to query for reviews
        Toy=Toy
    )


@app.route('/profile/<int:user_id>')
def other_profile(user_id):
    """A function that directs users to other users profile pages"""
    # Get the logged in user for security check
    logged_in_user = session.get("user_id")
    # Get the user id to populate profile
    user = Users.query.get_or_404(user_id)
    # Find the user profile based on user_id
    user_profile = Profile.query.filter_by(user_id=user_id).first_or_404()
    # Get all countries
    country = pycountry.countries
    # If there is a current value for country, make the flag url
    if user_profile.country:
        flag_url = "/static/img/flags/" + user_profile.country.lower() + ".svg"
    else:
        flag_url = None
    # Get the user reviews
    reviews = Review.query.filter_by(user_id=user.id).order_by(Review.id).all()
    # Get the sort options with default value
    sort_option = request.args.get('sort', 'newest_first')
    # Set sorting order
    if sort_option == 'newest_first':
        reviews = Review.query.filter_by(user_id=user.id).order_by(Review.id.desc()).all()
    elif sort_option == 'oldest_first':
        reviews = Review.query.filter_by(user_id=user.id).order_by(Review.id.asc()).all()         
    elif sort_option == 'rating_asc':
        reviews = Review.query.filter_by(user_id=user.id).order_by(Review.rating.asc()).all()
    elif sort_option == 'rating_desc':
        reviews = Review.query.filter_by(user_id=user.id).order_by(Review.rating.desc()).all()
    return render_template(
        'profile.html',
        logged_in_user=logged_in_user,
        user=user,
        user_profile=user_profile,
        flag_url=flag_url,
        reviews=reviews,
        sort_option=sort_option,
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
    # Get the logged in user for security check
    logged_in_user = session.get("user_id")
    # Gets the previous page for back button
    referer = request.headers.get("Referer")
    # Back button user to home if they accessed page via URL
    if not referer:
        referer = url_for('home')
    # Get the user the profile belongs to
    user = Users.query.get_or_404(user_id)
    # Get the users profile
    profile = Profile.query.filter_by(user_id=user_id).first_or_404()
    # Get a list of countrys from pycountry library
    countries = sorted(pycountry.countries, key=lambda country: country.name)
    # Populate the country select element
    country_choices = [
        (country.alpha_2, country.name) for country in countries
    ]
    # Sets the form and the country choices
    form = EditProfile(obj=profile)
    form.country.choices = country_choices
    # If there are no errors in the form when submitted:
    if form.validate_on_submit():
        # Set default for empty about me section:
        if form.about_me.data.strip() == '':
            profile.about_me = "I am yet to fill this out."
        else:
            profile.about_me = form.about_me.data
        profile.is_parent = form.is_parent.data
        profile.country = form.country.data
        # Set a default user image if none selected
        if form.user_image.data.strip() == '':
            profile.user_image = "/static/img/default_profile_image.webp"
        else:
            profile.user_image = form.user_image.data
        # Saves these changes
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template(
        'edit_profile.html',
        logged_in_user=logged_in_user,
        referer=referer,
        user=user,
        profile=profile,
        countries=countries,
        form=form
    )


@app.route('/change_password/<int:user_id>', methods=['GET', 'POST'])
def change_password(user_id):
    """
    A function that directs users to the change password page.
    Utilizes the ChangePassword form to get user data.
    Validates the password and updates the user password.
    Redirects user to edit profile page on successful signup.
    """
    # Get logged in user for security
    logged_in_user = session.get("user_id")
    # Get the previous page
    referer = request.headers.get("Referer")
    # Get the user
    user = Users.query.get_or_404(user_id)
    # Set the form
    form = ChangePassword()
    # If there are no errors in the form when submitted:
    if form.validate_on_submit():
        # Set values
        old_password = form.old_password.data
        new_password = form.new_password.data
        confirm_password = form.confirm_password.data
        # Check if the old password is correct
        if check_password_hash(user.password, old_password):
            # Validate new password requirements
            if len(new_password) < 8:
                flash('Password must be at least 8 characters long.')
            elif not re.search("[A-Z]", new_password):
                flash('Password must contain at least one uppercase letter.')
            elif not re.search("[0-9]", new_password):
                flash('Password must contain at least one digit.')
            elif not re.search("[!@#$%^&*(),.?\":{}|<>]", new_password):
                flash('Password must contain at least one special character.')
            elif new_password != confirm_password:
                flash('New password and confirm password do not match.')
            else:
                new_password_hash = generate_password_hash(
                    new_password,
                    # Password-Based Key Derivation Function 2 (PBKDF2)
                    # with the SHA-256 hash function.
                    # For securely storing the password.
                    method='pbkdf2:sha256',
                    # 8 byte long random value to be
                    # added before the hashed password.
                    salt_length=8
                )
                user.password = new_password_hash
                # Save the changes
                db.session.commit()
                return redirect(url_for('edit_profile', user_id=user_id))
        # If the old password is incorrect:
        else:
            flash('Incorrect old password. Please try again.')
    else:
        # Display errors for change password form
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"{field.capitalize()} error: {error}")
    return render_template(
        'change_password.html',
        logged_in_user=logged_in_user,
        referer=referer,
        user=user,
        form=form
    )


@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    """A function used to remove the user from Users table in the database."""
    # Gets the correct User
    user = Users.query.get_or_404(user_id)
    # Deletes the user
    db.session.delete(user)
    db.session.commit()
    # Logs out
    session.pop('user_id', None)
    # Redirects back to home.
    return redirect(url_for('home'))


@app.route("/toys")
def toys():
    """
    A function that directs users to the toy page.
    Provides a list of toys in the Toy table allowing the page to display
    all of the toys.
    Provides the user id of the logged in user in order to redirect
    logged out users to the homepage.
    Allows the page to be sorted as the users preference.
    """
    # Get logged in user for security check
    user_id = session.get('user_id')
    # Get all toys
    toys = list(Toy.query.order_by(Toy.name).all())
    # Display toy_types as a dictionary so as to assign to the toy.toy_type_id
    toy_types = {toy_type.id: toy_type for toy_type in ToyType.query.all()}
    # Get users sorting preference and default value
    sort_option = request.args.get('sort', 'name_asc')
    # Set sorting order
    if sort_option == 'name_asc':
        toys = Toy.query.order_by(Toy.name.asc()).all()
    elif sort_option == 'name_desc':
        toys = Toy.query.order_by(Toy.name.desc()).all()
    elif sort_option == 'type_asc':
        toys = Toy.query.join(ToyType).order_by(ToyType.toy_type.asc()).all()
    elif sort_option == 'type_desc':
        toys = Toy.query.join(ToyType).order_by(ToyType.toy_type.desc()).all()
    elif sort_option == 'company_asc':
        toys = Toy.query.order_by(Toy.company.asc()).all()
    elif sort_option == 'company_desc':
        toys = Toy.query.order_by(Toy.company.desc()).all()
    elif sort_option == 'rating_asc':
        # Get the ratings in order
        toys = Toy.query.all()
        # Create list of onluy ratings
        averages = []
        for toy in toys:
            averages.append(toy.average_rating())
        # Create dictionary of toy : rating
        toys_dict = {key: value for key, value in zip(toys, averages)}
        # Sort the dictionary
        sorted_toys = {key: value for key, value in sorted(
            toys_dict.items(),
            key=lambda item: item[1]
        )}
        # Get only the keys in the dictionary
        toys = list(sorted_toys.keys())
    elif sort_option == 'rating_desc':
        # Get the ratings in opposite order
        toys = Toy.query.all()
        # Create a list of only ratings
        averages = []
        for toy in toys:
            averages.append(toy.average_rating())
        # Create dictionary of toy : rating
        toys_dict = {key: value for key, value in zip(toys, averages)}
        # Sort the dictionary in reverse order
        sorted_toys = {key: value for key, value in sorted(
            toys_dict.items(),
            key=lambda item: item[1],
            reverse=True
        )}
        # Get only the keys in the dictionary
        toys = list(sorted_toys.keys())
    # Get the search bar query
    search_query = request.args.get('search_query', '')
    if search_query:
        # Join the ToyType table to search toy types too
        toys = Toy.query.join(ToyType).filter(
            or_(
                # Toy name 
                Toy.name.ilike(f'%{search_query}%'),
                # Toy company
                Toy.company.ilike(f'%{search_query}%'),
                # Toy type
                ToyType.toy_type.ilike(f'%{search_query}%')
            )
        ).all()
    return render_template(
        "toys.html",
        user_id=user_id,
        toys=toys,
        toy_types=toy_types,
        sort_option=sort_option
    )


@app.route('/toy/<int:toy_id>')
def individual_toy(toy_id):
    """
    A function that directs users to individual toy pages.
    Provides a list of information for the specific toy to display to users.
    Provides the user id of the logged in user in order to redirect
    logged out users to the homepage.
    """
    # Get logged in user for security check
    user_id = session.get('user_id')
    # Gets the previous page for back button
    referer = request.headers.get("Referer")
    # Back button redirects user to home if they accessed page via URL
    if not referer:
        referer = url_for('home')
    # Get the toy types
    toy_types = {toy_type.id: toy_type for toy_type in ToyType.query.all()}
    # Get the individual toy
    toy = Toy.query.get_or_404(toy_id)
    # Get the associated reviews
    reviews = Review.query.filter_by(toy_id=toy.id).order_by(Review.id).all()
    # Check if the user has already submitted a review
    already_reviewed = Review.query.filter_by(
        user_id=user_id,
        toy_id=toy.id
    ).first()
    # Get the sort options with default value
    sort_option = request.args.get('sort', 'rating_desc')
    # Set sorting order
    if sort_option == 'rating_asc':
        reviews = Review.query.filter_by(toy_id=toy.id).order_by(Review.rating.asc()).all()
    elif sort_option == 'rating_desc':
        reviews = Review.query.filter_by(toy_id=toy.id).order_by(Review.rating.desc()).all()
    return render_template(
        'individual_toy.html',
        user_id=user_id,
        referer=referer,
        toy_types=toy_types,
        toy=toy,
        reviews=reviews,
        already_reviewed=already_reviewed,
        sort_option=sort_option,
        Users=Users,
        Toy=Toy
    )


@app.route('/add_toy', methods=['GET', 'POST'])
def add_toy():
    """
    A function that directs users to the add toy page.
    Utilizes the AddToy form to get user data.
    Creates a new entry in the Toy table in the database.
    Redirects user to toys page on successful addition of a new toy.
    """
    # Get the logged in user for security check
    user_id = session.get('user_id')
    # Get the toy_types to populate select element
    toy_types = ToyType.query.all()
    # Get the add toy form
    form = AddToy()
    # Populate the toy type options
    form.toy_type_id.choices = [('0', "Select Toy Type")] + [
        (toy_type.id, toy_type.toy_type) for toy_type in toy_types
    ]
    # If there are no errors in the form when submitted:
    if form.is_submitted():
        # Check if a toy type was not selected
        if form.toy_type_id.data == 0:
            flash('Please select the toy type.')
        # If a toy type was selected, validate the form
        elif form.validate():
            # Set a default toy image if none provided
            if form.image_url.data.strip() == '':
                form.image_url.data = "/static/img/default_toy.webp"
            # Set a default description if none provided
            if not form.description.data:
                form.description.data = "No description added yet."
            # New Toy class instance with submitted data
            new_toy = Toy(
                user_id=user_id,
                name=form.name.data.title(),
                company=form.company.data.title(),
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
    # Get the logged in user for security check and database info
    user_id = session.get("user_id")
    # Gets the toy to be edited
    toy = Toy.query.get_or_404(toy_id)
    # Gets the previous page for the back button
    referer = request.headers.get("Referer")
    # Back button redirects user to home if they accessed page via URL
    if not referer:
        referer = url_for('home')
    # Gets the edit toy form
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
        toy.name = form.name.data.title()
        toy.company = form.company.data.title()
        toy.toy_type_id = form.toy_type_id.data,
        # Set a default toy image if none provided
        if form.image_url.data.strip() == '':
            form.image_url.data = "/static/img/default_toy.webp"
        else:
            toy.image_url = form.image_url.data,
        # Set default text for empty description
        if not form.description.data:
            form.description.data = "No description added yet."
        else:
            toy.description = form.description.data
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
        user_id=user_id,
        toy=toy,
        referer=referer,
        form=form,
        toy_types=toy_types
    )


def remove_toy_from_reviews(review):
    """
    A function to remove the toy id from the also_liked list
    in the user reviews
    """
    updated_also_liked = []
    # Loop through also_liked and if they still exist, add to updated list
    for toy_id in review.also_liked:
        toy = Toy.query.filter_by(id=toy_id).first()
        if toy:
            updated_also_liked.append(toy_id)
    # Set also_liked as the updated list
    review.also_liked = updated_also_liked


@app.route('/delete_toy/<int:toy_id>')
def delete_toy(toy_id):
    """A function used to remove the toy from Toy table in the database."""
    # Gets the correct toy
    toy = Toy.query.get_or_404(toy_id)
    # Deletes the toy
    db.session.delete(toy)
    # Get all reviews
    reviews = Review.query.all()
    # Loop through them and if they have this toy id in also_liked, remove it
    for review in reviews:
        if toy_id in review.also_liked:
            remove_toy_from_reviews(review)
    # saves changes
    db.session.commit()
    # Redirects back to toys
    return redirect(url_for('toys'))


@app.route('/add_review/<int:toy_id>', methods=['GET', 'POST'])
def add_review(toy_id):
    """
    A function that directs users to the add review page.
    Utilizes the AddReview form to get user data.
    Creates a new entry in the Review table in the database
    Redirects user to individual toy page on successful addition of review.
    """
    # Get the current user for security and Review table
    user_id = session.get('user_id')
    # Gets the previous page for back button
    referer = request.headers.get("Referer")
    # Back button redirects user to home if they accessed page via URL
    if not referer:
        referer = url_for('home')
    # Get the toy that is being reviewed
    toy = Toy.query.get_or_404(toy_id)
    # Get all toys and use it to populate the also_liked selection
    toys = Toy.query.order_by(Toy.name).all()
    # Makes the toy options but removes the toy that the review is for
    toy_options = [(each_toy.id, each_toy.name) for each_toy in toys if each_toy.id != toy_id]
    # Set the form
    form = AddReview()
    # Set the also_liked selection choices
    form.also_liked.choices = toy_options
    # Check if the user has already submitted a review
    already_reviewed = Review.query.filter_by(
        user_id=user_id,
        toy_id=toy_id
    ).first()
    # If there are no errors in the form when submitted:
    if form.is_submitted():
        # Flash an error if a rating is not given
        if form.rating.data == '':
            flash('Please rate the toy.')
        elif form.validate():
            # New Review class instance with submitted data
            new_review = Review(
                user_id=user_id,
                toy_id=toy_id,
                review_content=form.review_content.data,
                rating=form.rating.data,
                also_liked=form.also_liked.data
            )
            # Adds the new review to the database and saves it
            db.session.add(new_review)
            db.session.commit()
            # Redirects user back to toy when the review is added
            return redirect(url_for('individual_toy', toy_id=toy_id))
    return render_template(
        'add_review.html',
        referer=referer,
        toy=toy,
        form=form,
        already_reviewed=already_reviewed
    )


@app.route('/edit_review/<int:review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    """
    A function that directs users to the edit review page.
    Utilizes the EditReview form to get user data.
    Updates the entry in the Review table in the database with new data.
    Redirects user back to the individual toy page.
    """
    # Get the user id for security
    user_id = session.get('user_id')
    # Gets the previous page for the back button
    referer = request.headers.get("Referer")
    # Back button redirects user to home if they accessed page via URL
    if not referer:
        referer = url_for('home')
    # Get the href ref for redirection on submission:
    ref = request.args.get('ref')
    # Get the review to be edited
    review = Review.query.get_or_404(review_id)
    # Get the toy that the review is for in order to redirect back to toy page
    toy = Toy.query.get_or_404(review.toy_id)
    toy_id = toy.id
    # Get all toys to populate the also_liked selection
    toys = Toy.query.all()
    toy_options = [(each_toy.id, each_toy.name) for each_toy in toys]
    # Select form to use and default values
    form = EditReview(
        review_content=review.review_content,
        rating=review.rating,
        also_liked=review.also_liked
    )
    # Set the also_liked selection choices
    form.also_liked.choices = toy_options
    if form.is_submitted():
        # Check that a rating is provided
        if form.rating.data == '':
            flash('Please rate the toy.')
        # If rating is provided, validate the form
        elif form.validate():
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
    return render_template(
        'edit_review.html',
        user_id=user_id,
        referer=referer,
        review=review,
        toy=toy,
        form=form
    )


@app.route('/delete_review/<int:review_id>')
def delete_review(review_id):
    """
    A function used to remove the review
    from Review table in the database.
    """
    user_id = session.get("user_id")

    # Gets the reference of the link
    ref = request.args.get('ref')
    # Gets the correct review
    review = Review.query.get_or_404(review_id)
    # Gets the toy id for redirection after deletion
    toy = Toy.query.get_or_404(review.toy_id)
    toy_id = toy.id
    # Deletes the review
    db.session.delete(review)
    db.session.commit()
    if ref == 'profile':
        # Redirects back to profile
        return redirect(url_for('other_profile', user_id=user_id))
    else:
        # Redirects back to toy.
        return redirect(url_for('individual_toy', toy_id=toy_id))


@app.route('/403')
def error403():
    """A function that directs users to the error 403 page"""
    return render_template('403.html')


@app.route('/500')
def error500():
    """A function that directs users to the error 500 page"""
    return render_template('500.html')


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


@app.errorhandler(403)
def access_restricted(e):
    """
    Redirects to a 403 page when the user tries
    to access something without permission
    """
    # Directs the user and provides HTTP staus code
    return render_template('403.html'), 403
