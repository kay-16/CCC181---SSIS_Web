from flask import Blueprint
from flask import Flask, render_template
from app.students.controller import get_all_students

students = Blueprint('students', __name__)

@students.route("/students")  
def student():
    students = get_all_students()
    return render_template('student/student.html', title='Student', students = students)