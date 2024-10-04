from flask import render_template, request, url_for, redirect, flash
from app.programs.controller import get_programs, get_college, add_program_to_db, search_programs, edit_programs, get_program_by_code, check_course_code_exists, delete_programs
from app.programs.forms import ProgramForms, EditProgramForms
from . import programs


@programs.route("/programs")  
def program():
    try:
        programs = get_programs() # Fetch all student from the database

    except Exception as e:
        flash(f"An error has occured while fetching programs: {e}", "danger")
        return redirect(url_for('programs.program'))    # Redirect back to the student list in case of error
    return render_template('program/program.html', title='Programs', programs=programs)


@programs.route("/programs/add", methods=["POST", "GET"])
def add_program():
    form = ProgramForms()

    try:
        college = get_college()   # Fetch colleges
        if college:
            form.college_belong.choices = [(college[0], f"{college[0]} - {college[1]}") for college in college]

    except Exception as e:
        flash(f"An error has occurred while fetching colleges: {e}", "danger")
        return redirect(url_for('programs.add_program'))    # Redirect back to the program list in case of error
    
    if form.validate_on_submit():

        try:
            # Checks if college code entered already exists 
            if check_course_code_exists(form.program_code.data):
                flash(f"Program code {form.program_code.data} already exists. Please enter a different code.", "danger")
                return redirect(url_for('programs.add_program'))


        # Insert the added program into the database
            program_data = (
                form.program_code.data,
                form.program_name.data,
                form.college_belong.data
            )

            add_program_to_db(program_data)
            flash(f'Added {form.program_code.data} with name {form.program_name.data} under the {form.college_belong.data}!', 'success')
            return redirect(url_for('programs.program')) # If validated, redirect user back to student page
        
        except Exception as e:
            flash(f"An error has occurred while adding the program: {e}", "danger")

    return render_template('program/program_form.html', title='Program | Add', form=form, page_title="Add Program")


@programs.route("/programs/search", methods=["GET"])  
def search_program():
    # fetch parameters
    column_name = request.args.get("column-search", "col_course_code")
    searched_data =  request.args.get("search-query", "")

    try:
        if searched_data:
            program = search_programs(column_name, searched_data)
            return render_template('program/program.html', programs=program, searched_data=searched_data, column_name=column_name)
        
    except Exception as e:
        flash(f"An error has occured while searching for programs: {e}", "danger")
          
    return redirect(url_for('programs.program'))


@programs.route("/programs/edit/<code>", methods=["POST", "GET"])
def edit_program(code):
    try:
        program = get_program_by_code(code) # Fetch student by their ID number
        if not program:
            flash("Program Not Found", "danger")
            return redirect(url_for('programs.program'))
    except Exception as e:
        flash(f"An error has occured while fetching programs: {e}", "danger")
        return redirect(url_for('programs.program'))  
    
    form = EditProgramForms()
    
    try:
        college = get_college()   # Fetch colleges
        if college:
            form.college_belong.choices = [(college[0], f"{college[0]} - {college[1]}") for college in college]

    except Exception as e:
        flash(f"An error has occured while fetching programs: {e}", "danger")
         
    if request.method == 'POST' and form.validate_on_submit():
        try:
            # Checks if course code entered already exists and;
            # Checks if the course code entered is different from original 
            if form.program_code.data != code and check_course_code_exists(form.program_code.data):
                flash(f"Program code {form.program_code.data} already exists. Please enter a different program code.", "danger")
                return redirect(url_for('programs.edit_program', code=code))
            
            # Prepare data for update
            program_data = (
                form.program_code.data,
                form.program_name.data,
                form.college_belong.data,    
                code  # The code of the program to update
            )

            edit_programs(program_data) # Calls edit function
            flash("Program updated successfully", "success")
            return redirect(url_for('programs.program'))  # Redirect back to program list after edit
        except Exception as e:
            flash(f"An error has occured while updating the program: {e}", "danger")
    
    # Prepopulate form with the program's existing data
    form.program_code.data = program[0]
    form.program_name.data = program[1]
    form.college_belong.data = program[2]
    
    return render_template('program/edit_program_form.html', title='Program | Edit', form=form, program=program)


@programs.route("/programs/delete/<prog_code>", methods=["POST"])
def delete_program(prog_code):
    if request.method == "POST":
        try:
            program = get_program_by_code(prog_code) # Fetch program by their program code
            if not program:
                flash("Program Not Found", "danger")
                return redirect(url_for('programs.program'))
                
            delete_programs(prog_code)
            flash(f"Program with code {prog_code} is deleted successfully!", "success")

        except Exception as e:
            flash(f"Database error: {str(e)}", "danger")

    else: # Prevents user from attempting to delete a program in the URL
        flash(f"WARNING: Do not attempt to delete a program directly via URL!", "danger")

    return redirect(url_for('programs.program'))
