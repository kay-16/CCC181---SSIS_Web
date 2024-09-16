from flask import Blueprint
from flask import Flask, render_template

programs = Blueprint('programs', __name__)

@programs.route("/programs")  
def program():
    return render_template('program/program.html', title='Programs')