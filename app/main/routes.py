from flask import render_template
from . import main

# Route for home page
@main.route("/")  
@main.route("/home") 
def home():
    return render_template('index.html')