from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError


class ProgramForms(FlaskForm):
    program_code = StringField('Program Code', validators=[
        DataRequired(message="Provide a program code"), 
        Length(min=3, max=20, message="Program code must be at least 3 characters minimum and 20 characters maximum."),
        ], render_kw={"placeholder": "Enter a Program Code (e.g. BSE)"})
    
    program_name = StringField('Program Name', validators=[DataRequired(message="Please fill out this field."), Length(min=8, max=200)],
                             render_kw={"placeholder": "Enter a Program Name (e.g. Bachelor of Science in Economics)"})
    
    college_belong = SelectField('College', choices=[])
    
    submit = SubmitField('Submit')


class EditProgramForms(FlaskForm):
    program_code = StringField('Program Code', validators=[
        DataRequired(message="Provide a program code"), 
        Length(min=3, max=20, message="Program code must be at least 3 characters minimum and 20 characters maximum."),
        ], render_kw={"placeholder": "Enter a Program Code (e.g. BSE)"})
    
    program_name = StringField('Program Name', validators=[DataRequired(message="Please fill out this field."), Length(min=8, max=200)],
                             render_kw={"placeholder": "Enter a Program Name (e.g. Bachelor of Science in Economics)"})
    
    college_belong = SelectField('College', choices=[])
    
    save = SubmitField('Save Changes')
    cancel = SubmitField('Cancel')
