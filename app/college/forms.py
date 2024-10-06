from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class CollegeForms(FlaskForm):
    college_code = StringField('College Code', validators=[
        DataRequired(message="Please fill out this field. "), 
        Length(min=2, max=50, message="College code must be at least 2 characters minimum and 50 characters maximum."),  
        Regexp(regex="^[A-Z]+$", message="Use capital letters only and no spaces allowed.")
        ],
        render_kw={"placeholder": "Enter college code (e.g. CCS)"})
    
    college_name = StringField('College Name', validators=[
        DataRequired(message="Please fill out this field."), 
        Length(min=10, max=300),
        ],
        render_kw={"placeholder": "Enter college name (e.g. College of Computer Studies)"})
    
    submit = SubmitField('Submit')


class EditCollegeForms(FlaskForm):
    college_code = StringField('College Code', validators=[
        DataRequired(message="Please fill out this field."), 
        Length(min=2, max=50, message="College code must be at least 2 characters minimum and 50 characters maximum."),  
        Regexp(regex="^[A-Z]+$", message="Use capital letters only and no spaces allowed.")
        ],
        render_kw={"placeholder": "Enter college code (e.g. CCS)"})
    
    college_name = StringField('College Name', validators=[
        DataRequired(message="Please fill out this field."), 
        Length(min=10, max=300),
        ],
        render_kw={"placeholder": "Enter college name (e.g. College of Computer Studies)"})
    
    save = SubmitField('Submit')