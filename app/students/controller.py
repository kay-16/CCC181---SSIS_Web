from app import mysql

# Fetch all students from the database
def get_all_students():
    C = mysql.connection.cursor()
    try:
        C.execute("SELECT id_format, last_name, first_name, year_lvl, sex, stud_course_code FROM student ORDER BY last_name, first_name ASC;")
        rows = C.fetchall()
        return rows
    except Exception as e:
        print(f"An error occurred: {e}")
        return None # Return None or handle the error as needed
    finally:
        if C:   # Check if C is not None before closing
            C.close()   
    

# Fetch all programs from the database
def get_all_programs():
    C = mysql.connection.cursor()
    try:
        C.execute("SELECT course_code, course_name, college_belong FROM program ORDER BY course_code, course_name ASC;")
        rows = C.fetchall()
        return rows
    except Exception as e:
        print(f"An error occurred: {e}")
        return None # Return None or handle the error as needed
    finally:
        if C:   # Check if C is not None before closing
            C.close()   
        
# Adds the student to the database
def add_student_to_db(student):
    C = mysql.connection.cursor()
    try:
        insert_statement = """
            INSERT INTO student (id_format, first_name, last_name, year_lvl, sex, stud_course_code) 
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        C.execute(insert_statement, student)
        mysql.connection.commit()
    except Exception as e:
        mysql.connection.rollback()  # Rollback in case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Ensure the cursor is closed




# Search students by all information
#def search_students():
    #C = mysql.connection.cursor()
    #try:
         # //execute query to fetch student data by their ID no.
        #s_query = "SELECT * FROM student WHERE ID_number = %s OR student_name = %s OR gender = %s OR year_lvl = %s OR course_code = %s"

    #finally:
        

def edit_students(student):
    try:
        C  = mysql.connection.cursor()
        edit_statement = """
                        UPDATE `students` 
                        SET `id_format` = %s, `first_name` = %s, `last_name` = %s, `year_lvl` = %s, `sex` = %s, `stud_course_code` = %s 
                        WHERE `id_format` = %s;
                        """
        C .execute(edit_statement, student)
        mysql.connection.commit()
    except mysql.connection.Error as e:
        mysql.connection.rollback()  # Rollback in case of error
        raise e
    finally:
        C .close()  # Ensure the cursor is closed

