from flask import render_template
from . import programs


@programs.route("/programs")  
def program():
    return render_template('program/program.html', title='Programs')