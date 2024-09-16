from flask import Blueprint
from flask import Flask, render_template

students = Blueprint('students', __name__)

@students.route("/student")  
def student():
    return render_template('student/student.html', title='Student')