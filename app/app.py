from flask import Flask, render_template, url_for, flash, redirect
from .forms import RegistrationForm, LoginForm
from config import SECRET_KEY, DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, BOOTSTRAP_SERVE_LOCAL
from flask_mysqldb import MySQL


app = Flask(__name__) #__name__ (name of the module)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['DB_NAME'] = DB_NAME
app.config['DB_USERNAME'] = DB_USERNAME
app.config['DB_PASSWORD'] = DB_PASSWORD
app.config['DB_HOST'] = DB_HOST
app.config['BOOTSTRAP_SERVE_LOCAL'] = BOOTSTRAP_SERVE_LOCAL


@app.route("/")  
def home():
    return render_template('home/home_page.html')

#@app.route("/student")  
#def student():
 #   return render_template('student/student.html', title='Student')

@app.route("/program")  
def program():
    return render_template('program/program.html', title='Programs')

@app.route("/college")  
def college():
    return render_template('college/college.html', title='College')

# create route for registration 
@app.route("/register", methods=['GET', 'POST'])  
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #alert form; 2nd argument:'success' a category of flash function
        flash(f'Account created for {form.username.data}!', 'success') 
        # if validated, redirect the user to the home page
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

# create route for login 
@app.route("/login", methods=['GET', 'POST'])  
def login():
    form = LoginForm()
    if form.validate_on_submit(): # for now, this is the only email & password that is accepted
        if form.email.data == 'admin@ssis.com' and form.password.data == 'admin':
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Failed to login. Please check username and password', 'danger')
    return render_template('login.html', title='Log In', form=form)

