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


class LoginForm(FlaskForm):
    # use email for log in
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=2, max=20)])
    remember = BooleanField('Remember Me') # remember field to remember their acc
    submit = SubmitField('Log In')


#class StudentForms(FlaskForm):
    #id_number = StringField('ID Number', validators=[DataRequired(message="Provide an ID Number in this format: YYYY-NNNN e.g. 2021-1234"), Length(min=9, max=9), 
                               #                      Regexp(regex="\\d{4}-\\d{4}",message="Format not valid.")])
    
    #first_name = StringField('First Name', validators=[DataRequired(message="Fill out this field"), Length(min=2, max=60)])
    #last_name = StringField('Last Name', validators=[DataRequired(message="Fill out this field"), Length(min=2, max=60)])
    #stud_course_code = SelectField('Program', options=[])
    #year_lvl = SelectField('Year Level', options=[("1st Year","1st Year"),("2nd Year","2nd Year"),("3rd Year","3rd Year"),("4th Year","4th Year"),
    #                                              ("5th Year","5th Year"),("6th Year","6th Year")])
    #gender = StringField('Gender', validators=[DataRequired(message="Fill out this field"), Length(min=3, max=60)])