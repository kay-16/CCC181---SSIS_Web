from flask import Blueprint
from app.login.forms import LoginForm
from flask import Flask, render_template, url_for, flash, redirect


login = Blueprint('login', __name__)

# create route for login 
@login.route("/login", methods=['GET', 'POST'])  
def logins():
    form = LoginForm()
    if form.validate_on_submit(): # for now, this is the only email & password that is accepted
        if form.email.data == 'admin@ssis.com' and form.password.data == 'admin':
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('students.student'))
        else:
            flash('Failed to login. Please check username and password', 'danger')
    return render_template('login.html', title='Log In', form=form)
