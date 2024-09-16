from flask import Blueprint
from flask import Flask, render_template

main = Blueprint('main', __name__)

@main.route("/")  
@main.route("/home") 
def home():
    return render_template('home/home_page.html')