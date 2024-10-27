from flask import render_template, request, url_for, redirect, flash
from app.students.controller import get_all_students, get_all_programs, add_student_to_db, search_students, edit_students, get_student_by_id, delete_students, check_id_exists
from app.students.forms import StudentForms, EditStudentForms 
from . import students
import cloudinary.uploader


@students.route("/students")  
def student():
    try:
        students = get_all_students() # Fetch all student from the database

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
            form.stud_course_code.choices = [(None, "Unenrolled")] + [(program[0], f"{program[0]} - {program[1]}") for program in programs]

    except Exception as e:
        flash(f"An error has occurred while fetching students: {e}", "danger")
        return redirect(url_for('students.add_student'))    # Redirect back to the student list in case of error
    
    if form.validate_on_submit():

        try:    
        # Checks if ID entered already exists 
            if check_id_exists(form.id_number.data):
                flash(f"ID number {form.id_number.data} already exists. Please enter a different ID.", "danger")
                return redirect(url_for('students.add_student'))
            
        # Handle file upload
            image_file = form.student_image.data
            image_url = None
            if image_file:
                upload_result = cloudinary.uploader.upload(image_file)
                print(upload_result)
                image_url = upload_result.get('secure_url')

        # Insert the added student into the database
            student_data = (
                form.id_number.data,
                form.first_name.data,
                form.last_name.data,
                form.year_lvl.data,
                form.gender.data,
                form.stud_course_code.data if form.stud_course_code.data != 'None' else None,
                image_url       # Stores image URL if it was uploaded
            )

            add_student_to_db(student_data)

            flash(f'Added {form.first_name.data} {form.last_name.data} with ID number {form.id_number.data}!', 'success') 
            return redirect(url_for('students.student')) # If validated, redirect user back to student page
        
        except Exception as e:
            flash(f"An error has occurred while adding the student: {e}", "danger")
       
    return render_template('student/student_form.html', title='Student | Add', form=form, page_title="Add Student")


@students.route("/search", methods=["GET"])  
def search_student():
    # fetch parameters
    column_name = request.args.get("column-search", "id_format")
    searched_data =  request.args.get("search-query", "")

    try:
        if searched_data:
            student = search_students(column_name, searched_data)
            return render_template('student/student.html', students=student, searched_data=searched_data, column_name=column_name)
        
    except Exception as e:
        flash(f"An error has occured while searching for students: {e}", "danger")
          
    return redirect(url_for('students.student'))


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
            form.stud_course_code.choices = [(program[0], f"{program[0]} - {program[1]}") for program in programs]
            
    except Exception as e:
        flash(f"An error has occured while fetching programs: {e}", "danger")
         
    if request.method == 'POST' and form.validate_on_submit():
        try:
            # Checks if student ID entered already exists and;
            # Checks if the student ID entered is different from original 
            if form.id_number.data != id and check_id_exists(form.id_number.data):
                flash(f"ID number {form.id_number.data} already exists. Please enter a different ID.", "danger")
                return redirect(url_for('students.edit_student', id=id))
            
            # Handle file upload
            image_file = form.student_image.data
            image_url = None
            if form.remove_image.data:
                image_url = None    # Sets image URL to NULL (removed) in the database
            elif image_file:
                upload_result = cloudinary.uploader.upload(image_file)
                print(upload_result)
                image_url = upload_result.get('secure_url')
            else:
                image_url = student[6]    # Retain the current image if no image is removed or uploaded 

            # Prepare data for update
            student_data = (
                form.id_number.data,
                form.first_name.data,
                form.last_name.data,    
                form.year_lvl.data,
                form.gender.data,
                form.stud_course_code.data,
                image_url,
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

    return render_template('student/edit_student_form.html', title='Student | Edit', form=form, 
                           student=student, current_image_url=student[6])


@students.route("/delete/<id_num>", methods=["POST"])
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

""" 
@students.route("/upload_image", methods=["GET", "POST"])
def upload_image_student():
    form = UploadImageForms
    if form.validate_on_submit():
        image_file = request.files['image']
        if image_file:
            upload_result = cloudinary.uploader.upload('image_file')
            image_url = upload_result.get('secure_url')


            flash(f"Image uploaded successfully!", "success")
            return redirect(url_for('students.student'))
    return render_template('upload_image.html', form=form)
    """