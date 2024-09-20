from flask import Blueprint
from flask import Flask, render_template, request
from app.students.controller import get_all_students

students = Blueprint('students', __name__)

@students.route("/students")  
def student():
    students = get_all_students()
    return render_template('student/student.html', title='Student', students = students)

@students.route("/students/<int:id>/edit", methods=['GET', 'POST'])
def edit_student_route(id):
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