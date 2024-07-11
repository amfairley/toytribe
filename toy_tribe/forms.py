from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField, EmailField,
    SelectField,
    BooleanField,
    TextAreaField
)
from wtforms.validators import (
    DataRequired,
    Length,
    EqualTo,
    Email
)
import pycountry


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
    email = EmailField(
        'Email',
        validators=[DataRequired(), Email(), Length(max=120)]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Register')


class AddToy(FlaskForm):
    """
    AddToy class to handle toy creation functionality.
    Collects toy name, company name, toy type, apprval, and image url.
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
    image_url = StringField('Image URL')  # Not required, can be null
    submit = SubmitField('Add Toy')


class EditToy(FlaskForm):
    """
    EditToy class to handle toy updating functionality.
    Collects toy name, company, toy type, approval, and image url.
    """
    name = StringField('Toy Name', validators=[DataRequired()])
    company = StringField('Company Name', validators=[DataRequired()])
    toy_type_id = SelectField('Type of Toy', choices=[], coerce=int)
    description = TextAreaField('Toy Description')
    image_url = StringField('Image URL')
    submit = SubmitField('Edit Toy')


class EditProfile(FlaskForm):
    """
    EditProfile class to handle profile updating functionality.
    Collects about_me, country, is_parent, user_image.
    """
    about_me = TextAreaField('About Me')
    is_parent = BooleanField('Are you a parent?')
    country = SelectField('Country', choices=[], coerce=str)
    user_image = StringField('Profile Picture URL:')
    submit = SubmitField('Edit Profile')
