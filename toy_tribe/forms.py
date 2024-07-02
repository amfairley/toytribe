from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=4, max=150)])
    # username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=100)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    # username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')