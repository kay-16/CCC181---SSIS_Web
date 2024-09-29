from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp


class StudentForms(FlaskForm):
    id_number = StringField('ID Number', validators=[
        DataRequired(message="Provide an ID Number in this format: YYYY-NNNN e.g. 2021-1234"), 
        Length(min=9, max=9, message="ID format must be exactly 9 characters long"),  
        Regexp(regex="^\d{4}-\d{4}$", message="Format invalid. Use YYYY-NNNN (e.g. 2022-1209).")
        ],
        render_kw={"placeholder": "Enter ID number (e.g. 2022-1243)"})
    
    first_name = StringField('First Name', validators=[DataRequired(message="Fill out this field"), Length(min=2, max=60)],
                             render_kw={"placeholder": "Enter first name (e.g. Lanz)"})
    
    last_name = StringField('Last Name', validators=[DataRequired(message="Fill out this field"), Length(min=2, max=60)],
                            render_kw={"placeholder": "Enter last name (e.g. Santos)"})
    
    year_lvl = SelectField('Year Level', choices=[("1st Year","1st Year"),("2nd Year","2nd Year"),("3rd Year","3rd Year"),("4th Year","4th Year"),
                                                  ("5th Year","5th Year"),("6th Year","6th Year")])
    
    gender = SelectField('Sex', choices=[("Male","Male"),("Female","Female"),("Non-binary","Non-binary")])
    
    stud_course_code = SelectField('Program', choices=[])

    submit = SubmitField('Submit')
    
    
class EditStudentForms(FlaskForm):
    id_number = StringField('ID Number', validators=[
        DataRequired(message="Provide an ID Number in this format: YYYY-NNNN e.g. 2021-1234"), 
        Length(min=9, max=9, message="ID format must be exactly 9 characters long"),  
        Regexp(regex="^\d{4}-\d{4}$", message="Format invalid. Use YYYY-NNNN (e.g. 2022-1209).")
        ])
    
    first_name = StringField('First Name', validators=[DataRequired(message="Fill out this field"), Length(min=2, max=60)])
    
    last_name = StringField('Last Name', validators=[DataRequired(message="Fill out this field"), Length(min=2, max=60)])
    
    year_lvl = SelectField('Year Level', choices=[("1st Year","1st Year"),("2nd Year","2nd Year"),("3rd Year","3rd Year"),("4th Year","4th Year"),
                                                  ("5th Year","5th Year"),("6th Year","6th Year")])
    
    gender = SelectField('Sex', choices=[("Male","Male"),("Female","Female"),("Non-binary","Non-binary")])
    
    stud_course_code = SelectField('Program', choices=[])

    save = SubmitField('Save Changes')
    cancel = SubmitField('Cancel')