from flask import Blueprint

from .. import forms

student_bp = Blueprint('student',__name__, template_folder="app/templates/student")

from . import controller, forms