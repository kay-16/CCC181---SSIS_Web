from flask import render_template, request, url_for, redirect, flash
from app.college.controller import get_all_college, add_college_to_db, check_college_code_exists, search_colleges, get_college_by_code, edit_colleges, delete_colleges
from app.college.forms import CollegeForms, EditCollegeForms
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


@college.route("/college/search", methods=["GET"])  
def search_college():
    # fetch parameters
    column_name = request.args.get("column-search", "col_course_code")
    searched_data =  request.args.get("search-query", "")

    try:
        if searched_data:
            college = search_colleges(column_name, searched_data)
            return render_template('college/college.html', colleges=college, searched_data=searched_data, column_name=column_name)
        
    except Exception as e:
        flash(f"An error has occured while searching for colleges: {e}", "danger")
          
    return redirect(url_for('college.colleges'))


@college.route("/college/edit/<code>", methods=["POST", "GET"])
def edit_college(code):
    try:
        college = get_college_by_code(code) # Fetch college by their college code
        if not college:
            flash("College Not Found", "danger")
            return redirect(url_for('college.colleges'))
    except Exception as e:
        flash(f"An error has occured while fetching colleges: {e}", "danger")
        return redirect(url_for('college.colleges'))  
    
    form = EditCollegeForms()
          
    if request.method == 'POST' and form.validate_on_submit():
        try:
            # Checks if college code entered already exists and;
            # Checks if the college code entered is different from original 
            if form.college_code.data != code and check_college_code_exists(form.college_code.data):
                flash(f"College code {form.college_code.data} already exists. Please enter a different college code.", "danger")
                return redirect(url_for('college.edit_college', code=code))
            
            # Prepare data for update
            college_data = (
                form.college_code.data,
                form.college_name.data,  
                code  # The code of the program to update
            )

            edit_colleges(college_data) # Calls edit function
            flash("College updated successfully", "success")
            return redirect(url_for('college.colleges'))  # Redirect back to college list after edit
        except Exception as e:
            flash(f"An error has occured while updating the college: {e}", "danger")
    
    # Prepopulate form with the college's existing data
    form.college_code.data = college[0]
    form.college_name.data = college[1]
    
    return render_template('college/edit_college_form.html', title='College | Edit', form=form, college=college)


@college.route("/delete/<id_num>", methods=["POST"])
def delete_college(col_code):
    if request.method == "POST":
        try:
            college = get_college_by_code(col_code) # Fetch college by their college code
            if not college:
                flash("College Not Found", "danger")
                return redirect(url_for('college.colleges'))
                
            delete_colleges(col_code)
            flash(f"College {col_code} is deleted successfully!", "success")

        except Exception as e:
            flash(f"Database error: {str(e)}", "danger")

    else: # Prevents user from attempting to delete a college in the URL
        flash(f"WARNING: Do not attempt to delete a college directly via URL!", "danger")

    return redirect(url_for('college.colleges'))