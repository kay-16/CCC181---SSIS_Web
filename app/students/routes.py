from flask import Blueprint
from flask import Flask, render_template, request, url_for, redirect, flash
from app.students.controller import get_all_students, get_all_programs, add_student_to_db, search_students, edit_students, get_student_by_id
from app.students.forms import StudentForms, EditStudentForms

students = Blueprint('students', __name__)

@students.route("/students")  
def student():
    students = get_all_students()
    return render_template('student/student.html', title='Student', students=students)


@students.route("/add", methods=["POST", "GET"])  
def add_student():
    form = StudentForms()

    programs = get_all_programs()   # Fetch programs
    if programs:
        form.stud_course_code.choices = [(program[0], f"{program[0]}, {program[1]}") for program in programs]

    if form.validate_on_submit():
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
    
    return render_template('student/student_form.html', title='Student | Add', form=form, page_title="Add Student")



@students.route("/search", methods=["GET"])  
def search_student():
    query = request.args.get('query')

    if query: # Call the search_students function and pass the search query
        students = search_students(query)

    else:  # If no query, return all students or handle accordingly
        students = get_all_students()

    return render_template('student/student.html', students=students)


@students.route("/edit/<id>", methods=["POST", "GET"])
def edit_student(id):
    student = get_student_by_id(id) # Fetch student by their ID number
    if not student:
        flash("Student Not Found", "danger")
        return redirect(url_for('students.student'))
    
    form = EditStudentForms()
    
    programs = get_all_programs()   # Fetch programs
    if programs:
        form.stud_course_code.choices = [(program[0], f"{program[0]}, {program[1]}") for program in programs]


    if request.method == 'POST' and form.validate_on_submit():
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
    
    # Prepopulate form with the student's existing data
    form.id_number.data = student[0]
    form.first_name.data = student[1]
    form.last_name.data = student[2]
    form.year_lvl.data = student[3]
    form.gender.data = student[4]
    form.stud_course_code.data = student[5]


    return render_template('student/edit_student_form.html', title='Student | Edit', form=form, student=student)
    