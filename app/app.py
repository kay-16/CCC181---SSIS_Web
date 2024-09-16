from flask import Flask, render_template, url_for, flash, redirect
from config import SECRET_KEY, DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, BOOTSTRAP_SERVE_LOCAL
from flask_mysqldb import MySQL


app = Flask(__name__) #__name__ (name of module)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['DB_NAME'] = DB_NAME
app.config['DB_USERNAME'] = DB_USERNAME
app.config['DB_PASSWORD'] = DB_PASSWORD
app.config['DB_HOST'] = DB_HOST
app.config['BOOTSTRAP_SERVE_LOCAL'] = BOOTSTRAP_SERVE_LOCAL

mysql = MySQL(app)

@app.route("/")  
@app.route("/home") 
def home():
    return render_template('home/home_page.html')




