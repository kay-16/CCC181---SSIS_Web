from flask import render_template, request, url_for, redirect, flash
from app.college.controller import get_all_college, add_college_to_db, check_college_code_exists
from app.college.forms import CollegeForms
from . import college


@college.route("/college")  
def colleges():
    try:
        colleges = get_all_college() # Fetch all colleges from the database

    except Exception as e:
        flash(f"An error has occured while fetching colleges: {e}", "danger")
        return redirect(url_for('college.colleges'))    # Redirect back to the student list in case of error
    return render_template('college/college.html', title='College', colleges=colleges)


@college.route("/college/add", methods=["POST", "GET"])  
def add_college():
    form = CollegeForms()

    if form.validate_on_submit():

        try:    
        # Checks if college code entered already exists 
            if check_college_code_exists(form.college_code.data):
                flash(f"College code {form.college_code.data} already exists. Please enter a different code.", "danger")
                return redirect(url_for('college.add_college'))

        # Insert the added college data into the database
            college_data = (
                form.college_code.data,
                form.college_name.data
            )

            add_college_to_db(college_data)
            flash(f'Added {form.college_code.data} with college name {form.college_name.data}!', 'success') 
            return redirect(url_for('college.colleges')) # If validated, redirect user back to college page
        
        except Exception as e:
            flash(f"An error has occurred while adding the college: {e}", "danger")
       
    return render_template('college/college_form.html', title='College | Add', form=form, page_title="Add College")

