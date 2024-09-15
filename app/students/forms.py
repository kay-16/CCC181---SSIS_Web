from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp

class StudentForms(FlaskForm):
    id_number = StringField('ID Number', validators=[DataRequired(message="Provide an ID Number in this format: YYYY-NNNN e.g. 2021-1234"), Length(min=9, max=9), 
                                                     Regexp(regex="\\d{4}-\\d{4}",message="Format not valid.")])
    
    first_name = StringField('First Name', validators=[DataRequired(message="Fill out this field"), Length(min=2, max=60)])
    last_name = StringField('Last Name', validators=[DataRequired(message="Fill out this field"), Length(min=2, max=60)])
    stud_course_code = SelectField('Program', options=[])
    year_lvl = SelectField('Year Level', options=[("1st Year","1st Year"),("2nd Year","2nd Year"),("3rd Year","3rd Year"),("4th Year","4th Year"),
                                                  ("5th Year","5th Year"),("6th Year","6th Year")])
    gender = StringField('Gender', validators=[DataRequired(message="Fill out this field"), Length(min=3, max=60)])