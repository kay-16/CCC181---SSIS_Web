from flask import Blueprint

student_bp = Blueprint('student',__name__) 

from app.students import controller, routes
