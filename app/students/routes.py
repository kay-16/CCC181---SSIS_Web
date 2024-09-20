from flask import Blueprint
from flask import Flask, render_template, request, url_for, redirect, flash
from app.students.controller import get_all_students, get_all_programs, add_student_to_db
from app.students.forms import StudentForms

students = Blueprint('students', __name__)

@students.route("/students")  
def student():
    students = get_all_students()
    return render_template('student/student.html', title='Student', students = students)

"""
@students.route("/students/<int:id>/edit", methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        # Call the edit function with form data
        student_data = (
            request.form.get('id_format'),
            request.form.get('first_name'),
            request.form.get('last_name'),
            request.form.get('year_lvl'),
            request.form.get('sex'),
            request.form.get('stud_course_code'),
            id  # The ID of the student to update
        )
        edit_students(student_data)
        return redirect(url_for('students.student'))  # Redirect after edit
    
    # If GET request, fetch the student data
    student = get_student_by_id(id)  # Implement this function to fetch the student's current data
    return render_template('student/edit_student.html', student=student)
"""

@students.route("/add", methods=["POST", "GET"])  
def add_student():
    form = StudentForms()

    programs = get_all_programs()
    if programs:
        form.stud_course_code.choices = [(program[0], f"{program[0]}, {program[1]}") for program in programs]

    if form.validate_on_submit():
        # insert the added student into the database
        student_data = (
            form.id_number.data,
            form.first_name.data,
            form.last_name.data,
            form.year_lvl.data,
            form.gender.data,
            form.stud_course_code.data
        )

        add_student_to_db(student_data)

        # alert form
        flash(f'Added {form.first_name.data} {form.last_name.data} with ID number {form.id_number.data}!', 'success') 
        # if validated, redirect the user to the home page
        return redirect(url_for('students.student'))
    
    return render_template('student/studentForms.html', title='Student | Add', form=form, page_title="Add Student")


@students.route("/search", methods=["POST", "GET"])  
def search_student():
    query = request.args.get('query')

