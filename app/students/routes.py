from flask import Blueprint
from flask import Flask, render_template, request, url_for, redirect, flash
from app.students.controller import get_all_students, get_all_programs, add_student_to_db, search_students, edit_students, get_student_by_id, delete_students, check_id_exists
from app.students.forms import StudentForms, EditStudentForms

students = Blueprint('students', __name__)

@students.route("/students")  
def student():
    try:
        students = get_all_students()
    except Exception as e:
        flash(f"An error has occured while fetching students: {e}", "danger")
        return redirect(url_for('students.student'))    # Redirect back to the student list in case of error
    return render_template('student/student.html', title='Student', students=students)


@students.route("/add", methods=["POST", "GET"])  
def add_student():
    form = StudentForms()

    try:
        programs = get_all_programs()   # Fetch programs
        if programs:
            form.stud_course_code.choices = [(program[0], f"{program[0]}, {program[1]}") for program in programs]
    except Exception as e:
        flash(f"An error has occured while fetching students: {e}", "danger")
        return redirect(url_for('students.add_student'))    # Redirect back to the student list in case of error
    
    if form.validate_on_submit():
        try: 
        # Checks if ID entered already exists 
            if check_id_exists(form.id_number.data):
                flash(f"ID number {form.id_number.data} already exists. Please enter a different ID.", "danger")
                return redirect(url_for('students.add_student'))

        # Insert the added student into the database
            student_data = (
                form.id_number.data,
                form.first_name.data,
                form.last_name.data,
                form.year_lvl.data,
                form.gender.data,
                form.stud_course_code.data
            )

            add_student_to_db(student_data)
            flash(f'Added {form.first_name.data} {form.last_name.data} with ID number {form.id_number.data}!', 'success') 
            return redirect(url_for('students.student')) # If validated, redirect the user to the home page
        
        except Exception as e:
            flash(f"An error has occured while adding the student: {e}", "danger")
       
    return render_template('student/student_form.html', title='Student | Add', form=form, page_title="Add Student")



@students.route("/search", methods=["GET"])  
def search_student():
    query = request.args.get('query')

    try:
        if query: # Call the search_students function and pass the search query
            students = search_students(query)

        else:  # If no query, return all students or handle accordingly
            students = get_all_students()

    except Exception as e:
        flash(f"An error has occured while searching for students: {e}", "danger")
        return redirect(url_for('students.student'))  
    
    return render_template('student/student.html', students=students)



@students.route("/edit/<id>", methods=["POST", "GET"])
def edit_student(id):
    try:
        student = get_student_by_id(id) # Fetch student by their ID number
        if not student:
            flash("Student Not Found", "danger")
            return redirect(url_for('students.student'))
    except Exception as e:
        flash(f"An error has occured while fetching students: {e}", "danger")
        return redirect(url_for('students.student'))  
    
    form = EditStudentForms()
    
    try:
        programs = get_all_programs()   # Fetch programs
        if programs:
            form.stud_course_code.choices = [(program[0], f"{program[0]}, {program[1]}") for program in programs]
    except Exception as e:
        flash(f"An error has occured while fetching programs: {e}", "danger")
         
    if request.method == 'POST' and form.validate_on_submit():
        try:
            # Checks if ID entered already exists 
            if check_id_exists(form.id_number.data):
                flash(f"ID number {form.id_number.data} already exists. Please enter a different ID.", "danger")
                return redirect(url_for('students.edit_student', id=id))
            
            # Prepare data for update
            student_data = (
                form.id_number.data,
                form.first_name.data,
                form.last_name.data,    
                form.year_lvl.data,
                form.gender.data,
                form.stud_course_code.data,
                id  # The ID of the student to update
            )

            edit_students(student_data) # Calls edit function
            flash("Student updated successfully", "success")
            return redirect(url_for('students.student'))  # Redirect back to student list after edit
        except Exception as e:
            flash(f"An error has occured while updating the student: {e}", "danger")
    
    # Prepopulate form with the student's existing data
    form.id_number.data = student[0]
    form.first_name.data = student[1]
    form.last_name.data = student[2]
    form.year_lvl.data = student[3]
    form.gender.data = student[4]
    form.stud_course_code.data = student[5]

    return render_template('student/edit_student_form.html', title='Student | Edit', form=form, student=student)


@students.route("/delete/<id_num>", methods=["POST", "GET"])
def delete_student(id_num):
    if request.method == "POST":
        try:
            student = get_student_by_id(id_num) # Fetch student by their ID number
            if not student:
                flash("Student Not Found", "danger")
                return redirect(url_for('students.student'))
                
            delete_students(id_num)
            flash(f"Student {id_num} is deleted successfully!", "success")

        except Exception as e:
            flash(f"Database error: {str(e)}", "danger")

    else: # Prevents user from attempting to delete a student in the URL
        flash(f"WARNING: Do not attempt to delete a student directly via URL!", "danger")

    return redirect(url_for('students.student'))