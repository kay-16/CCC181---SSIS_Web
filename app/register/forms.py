from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)]) 
    # DataRequired() = makes sure the user don't leave username field empty
    # Length() = character limitation  

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', 
                             validators=[DataRequired(), Length(min=2, max=20), EqualTo('password')])
    
    submit = SubmitField('Sign Up')
