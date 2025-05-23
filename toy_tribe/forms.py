from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField, EmailField,
    SelectField,
    BooleanField,
    TextAreaField,
    SelectMultipleField
)
from wtforms.validators import (
    DataRequired,
    Length,
    EqualTo,
    Email,
    Length,
    Regexp
)
import pycountry
from toy_tribe.models import Toy


class SignupForm(FlaskForm):
    """
    SignupForm class to handle user signup functionality.
    Collects user's first name, last name, email, and password.
    """
    first_name = StringField(
        'First Name',
        validators=[DataRequired(), Length(min=1, max=100)]
    )
    last_name = StringField(
        'Last Name',
        validators=[DataRequired(), Length(min=1, max=100)]
    )
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(
                min=3,
                max=20,
                message='Username must be between 3 and 20 characters long'
            ),
            Regexp(
                '^[A-Za-z0-9_.]*$',
                message=(
                    "Username must contain only:\n"
                    " Letters,\n"
                    " numbers,\n"
                    " dots or underscores."
                )
            )
        ])
    email = EmailField(
        'Email',
        validators=[DataRequired(), Email(), Length(max=120)]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(
                min=8,
                message="Password must be at least 8 characters long."
            ),
            Regexp(
                r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
                message=(
                    "Password must contain:\n"
                    " An uppercase letter, \n"
                    " at least one number,\n"
                    " at least one special character."
                )
            )
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message="Passwords did not match.")
        ]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """
    LoginForm class for handling user login functionality.
    Collects user's email and password.
    """
    email = StringField(
        'Email',
        validators=[DataRequired(), Length(min=4, max=150)]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class EditProfile(FlaskForm):
    """
    EditProfile class to handle profile updating functionality.
    Collects about_me, country, is_parent, user_image.
    """
    about_me = TextAreaField('About Me')
    is_parent = BooleanField('Parent status:')
    country = SelectField('Country', choices=[], coerce=str)
    user_image = StringField('Profile Picture URL:')
    submit = SubmitField('Save Changes')


class ChangePassword(FlaskForm):
    """
    ChangePassword class to handle user changing thier password.
    Collects old_password, new_password and confirm_password.
    """
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField(
        'New Password',
        validators=[
            DataRequired(),
            Length(
                min=8,
                message="Password must be at least 8 characters long."
            ),
            Regexp(
                r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
                message=(
                    "Password must contain:\n"
                    " An uppercase letter, \n"
                    " at least one number,\n"
                    " at least one special character."
                )
            )
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo(
            'new_password',
            message="New passwords did not match."
        )]
    )
    submit = SubmitField('Change Password')


class AddToy(FlaskForm):
    """
    AddToy class to handle toy creation functionality.
    Collects toy name, company name, toy type, approval, and image url.
    """
    name = StringField('Toy Name', validators=[DataRequired()])
    company = StringField('Company Name', validators=[DataRequired()])
    toy_type_id = SelectField(
        'Type of Toy',
        choices=[],
        coerce=int,
        default='0',
    )
    description = TextAreaField('Toy Description')
    image_url = StringField('Image URL')
    submit = SubmitField('Add Toy')


class EditToy(FlaskForm):
    """
    EditToy class to handle toy updating functionality.
    Collects toy name, company, toy type, approval, and image url.
    """
    name = StringField('Toy Name', validators=[DataRequired()])
    company = StringField('Company Name', validators=[DataRequired()])
    toy_type_id = SelectField(
        'Type of Toy',
        choices=[],
        coerce=int,
        validators=[DataRequired()]
    )
    description = TextAreaField('Toy Description')
    image_url = StringField('Image URL')
    submit = SubmitField('Edit Toy')


class AddReview(FlaskForm):
    """
    AddReview class to handle review creation functionality.
    Collects review content, rating, also liked.
    """
    review_content = TextAreaField('Review', validators=[DataRequired()])
    rating = SelectField(
        'Star Rating',
        choices=[
            ('', 'Rate the toy!'),
            ('1', '1 Star'),
            ('2', '2 Stars'),
            ('3', '3 Stars'),
            ('4', '4 Stars'),
            ('5', '5 Stars')
        ],
        default=''
    )
    also_liked = SelectMultipleField('Also liked', choices=[], coerce=str)
    submit = SubmitField('Submit Review')


class EditReview(FlaskForm):
    """
    EditeReview class to handle review updating functionality.
    Collects review content, rating, also liked.
    """
    review_content = TextAreaField('Review', validators=[DataRequired()])
    rating = SelectField(
        'Star Rating',
        choices=[
            ('', 'Rate the toy!'),
            ('1', '1 Star'),
            ('2', '2 Stars'),
            ('3', '3 Stars'),
            ('4', '4 Stars'),
            ('5', '5 Stars')
        ]
    )
    also_liked = SelectMultipleField('Also liked', choices=[], coerce=str)
    submit = SubmitField('Submit Review')
