from flask import Blueprint
from flask import Flask, render_template

college = Blueprint('college', __name__)

@college.route("/college")  
def colleges():
    return render_template('college/college.html', title='College')