from flask import Blueprint
from app.register.forms import RegistrationForm
from flask import Flask, render_template, url_for, flash, redirect


register = Blueprint('register', __name__)

# create route for registration 
@register.route("/register", methods=['GET', 'POST'])  
def registers():
    form = RegistrationForm()
    if form.validate_on_submit():
        #alert form; 2nd argument:'success' a category of flash function
        flash(f'Account created for {form.username.data}!', 'success') 
        # if validated, redirect the user to the home page
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)