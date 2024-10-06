from app.login.forms import LoginForm
from flask import render_template, url_for, flash, redirect
from . import login

# create route for login 
@login.route("/login", methods=['GET', 'POST'])  
def logins():
    form = LoginForm()
    if form.validate_on_submit(): # Only accepts this email & password
        if form.email.data == 'admin@ssis.com' and form.password.data == 'admin':
            flash('You have successfully logged in. Welcome back, Kyla!', 'success')
            return redirect(url_for('students.student'))    # After logging in, redirects to student page
        else:
            flash('Failed to login. Please check username and password', 'danger')
    return render_template('login.html', title='Log In', form=form)
