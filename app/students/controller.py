#from app import mysql
from flask import Blueprint, render_template

student_bp = Blueprint('student', __name__)

@student_bp.route('/student')
def student():
    # Use local import to avoid circular import issue
    from app import mysql
    # Now you can use mysql here
    return render_template('student/student.html')

# Fetch all students from the database
