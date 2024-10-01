from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class CollegeForms(FlaskForm):
    college_code = StringField('College Code', validators=[
        DataRequired(message="Provide an ID Number in this format: YYYY-NNNN e.g. 2021-1234"), 
        Length(min=2, max=9, message="ID format must be exactly 9 characters long"),  
        Regexp(regex="^[A-Z]+$", message="Use capital letters only and no space allowed.")
        ],
        render_kw={"placeholder": "Enter college code (e.g. CCS)"})
    
    college_name = StringField('College Name', validators=[
        DataRequired(message="Please fill out this field."), 
        Length(min=10, max=300),
        ],
        render_kw={"placeholder": "Enter college name (e.g. College of Computer Studies)"})
    
    submit = SubmitField('Submit')