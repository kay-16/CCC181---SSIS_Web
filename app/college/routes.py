from flask import render_template
from . import college


@college.route("/college")  
def colleges():
    return render_template('college/college.html', title='College')