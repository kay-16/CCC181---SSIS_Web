from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError, Optional



class StudentForms(FlaskForm):
    id_number = StringField('ID Number', validators=[
        DataRequired(message="Provide an ID Number in this format: YYYY-NNNN (e.g. 2021-1234)."), 
        Length(min=9, max=9, message="ID format must be exactly 9 characters long."),  
        Regexp(regex="^\d{4}-\d{4}$", message="Format invalid. Use YYYY-NNNN (e.g. 2022-1209).")
        ],
        render_kw={"placeholder": "Enter ID number (e.g. 2022-1243)"})
    
    first_name = StringField('First Name', validators=[DataRequired(message="Please fill out this field."), Length(min=2, max=60)],
                             render_kw={"placeholder": "Enter first name (e.g. Bruce)"})
    
    last_name = StringField('Last Name', validators=[DataRequired(message="Please fill out this field."), Length(min=2, max=60)],
                            render_kw={"placeholder": "Enter last name (e.g. Wayne)"})
    
    year_lvl = SelectField('Year Level', choices=[("1st Year","1st Year"),("2nd Year","2nd Year"),("3rd Year","3rd Year"),("4th Year","4th Year")])
    
    gender = SelectField('Sex', choices=[("Male","Male"),("Female","Female"),("Non-binary","Non-binary")])
    
    stud_course_code = SelectField('Program', choices=[])

    # Limits file size to 2MB
    def FileSizeLimit(max_size_in_mb):
        max_size = max_size_in_mb*1024*1024

        def file_length_check(form, field):
            if not field.data:
                return
            if field.data.stream is None:
                return
            if len(field.data.read()) > max_size:
                raise ValidationError(f'File size is too large. Max allowed: {max_size_in_mb} MB.')
            field.data.seek(0)
        return file_length_check

    student_image = FileField('Upload Profile Picture', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'webp'],
                                                                       "⚠️ Not a valid image! Please upload a file in one of these formats: jpg, jpeg, png, or webp."),
                                                        FileSizeLimit(max_size_in_mb=2)
                                                        ])
    submit = SubmitField('Submit')

    
    
class EditStudentForms(FlaskForm):
    id_number = StringField('ID Number', validators=[
        DataRequired(message="Provide an ID Number in this format: YYYY-NNNN (e.g. 2021-1234)."), 
        Length(min=9, max=9, message="ID format must be exactly 9 characters long."),  
        Regexp(regex="^\d{4}-\d{4}$", message="Format invalid. Use YYYY-NNNN (e.g. 2022-1209).")
        ])
    
    first_name = StringField('First Name', validators=[DataRequired(message="Please fill out this field."), Length(min=2, max=60)])
    
    last_name = StringField('Last Name', validators=[DataRequired(message="Please fill out this field."), Length(min=2, max=60)])
    
    year_lvl = SelectField('Year Level', choices=[("1st Year","1st Year"),("2nd Year","2nd Year"),("3rd Year","3rd Year"),("4th Year","4th Year")])
    
    gender = SelectField('Sex', choices=[("Male","Male"),("Female","Female"),("Non-binary","Non-binary")])
    
    stud_course_code = SelectField('Program', choices=[])

    # Limits file size to 2MB
    def FileSizeLimit(max_size_in_mb):
        max_size = max_size_in_mb*1024*1024

        def file_length_check(form, field):
            if len(field.data.read()) > max_size:
                raise ValidationError(f'File size is too large. Max allowed: {max_size_in_mb} MB.')
            field.data.seek(0)
        return file_length_check

    student_image = FileField('Upload Profile Picture', validators=[Optional(),
                                                        FileAllowed(['jpg', 'jpeg', 'png', 'webp'],
                                                                       "⚠️ Not a valid image! Please upload a file in one of these formats: jpg, jpeg, png, or webp."),
                                                        FileSizeLimit(max_size_in_mb=2)
                                                        ])
    
    remove_image = BooleanField("Remove Image")
    save = SubmitField('Save Changes')
    
   