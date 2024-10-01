from flask import render_template, request, url_for, redirect, flash
from app.college.controller import get_all_college
from . import college


@college.route("/college")  
def colleges():
    try:
        colleges = get_all_college() # Fetch all colleges from the database

    except Exception as e:
        flash(f"An error has occured while fetching colleges: {e}", "danger")
        return redirect(url_for('college.colleges'))    # Redirect back to the student list in case of error
    return render_template('college/college.html', title='College', colleges=colleges)



