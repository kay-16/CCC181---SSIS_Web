from flask import Flask, render_template, url_for, flash, redirect
from flask_mysqldb import MySQL
from . import student_bp

@student_bp.route('/student', methods=['GET'])

def student():
    return render_template('student/student.html', title='Student')