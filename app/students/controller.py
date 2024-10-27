from app import mysql

# Fetch all students from the database
def get_all_students():
    C = mysql.connection.cursor()
    try:
        C.execute("SELECT * FROM student ORDER BY last_name ASC;")
        rows = C.fetchall()
        return rows
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None # Handle the error as needed
    finally:
        if C:   
            C.close()   # Close the cursor
    

# Fetch all programs from the database
def get_all_programs():
    C = mysql.connection.cursor()
    try:
        C.execute("SELECT course_code, course_name, college_belong FROM program ORDER BY course_code, course_name ASC;")
        rows = C.fetchall()
        return rows
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None # Handle the error as needed
    finally:
        if C:   
            C.close()   # Close the cursor
        

# Adds the student to the database
def add_student_to_db(student):
    C = mysql.connection.cursor()
    try:
        insert_statement = """
            INSERT INTO student (id_format, first_name, last_name, year_lvl, sex, stud_course_code, stud_image_url) 
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        C.execute(insert_statement, student)
        mysql.connection.commit()

    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor


# Checks for duplicated ID
def check_id_exists(id_number):
    C = mysql.connection.cursor()
    try:
        C.execute("""SELECT EXISTS(SELECT 1 FROM student WHERE id_format = %s);""", (id_number,))
        exists = C.fetchone()[0] > 0
        return exists
     
    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close() # Close the cursor


# Fetch the students according to the search parameters
def search_students(column, field):
    try:
        C = mysql.connection.cursor()
        if field == "Unenrolled":
            C.execute(f"SELECT * FROM student WHERE {column} IS NULL;")
        else:    
            C.execute(f"SELECT * FROM student WHERE {column} COLLATE utf8mb4_bin LIKE '%{field}%';")
        return C.fetchall()
    
    except mysql.connection.Error as e:
        mysql.connection.rollback()  # In case of error
        raise e
    finally:
        C.close()  # Close the cursor


# Fetch student data based on ID
def get_student_by_id(student_id):
    C  = mysql.connection.cursor()
    try: 
        get_statement = """ SELECT * FROM student WHERE id_format = %s """
        
        C.execute(get_statement, (student_id,))

        results = C.fetchone()
        return results

    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor


# Updates student data
def edit_students(student):
    C  = mysql.connection.cursor()
    try:
        edit_statement = """
                        UPDATE student
                        SET id_format = %s, first_name = %s, last_name = %s, year_lvl = %s, sex = %s, stud_course_code = %s, stud_image_url = %s 
                        WHERE id_format = %s;
                    """
        C.execute(edit_statement, student)
        mysql.connection.commit() 
        
    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor


# Removes student data based on ID number
def delete_students(stud_id):
    C  = mysql.connection.cursor()
    try:
        delete_statement = """ DELETE FROM student WHERE id_format = %s; """

        C.execute(delete_statement, (stud_id,))
        mysql.connection.commit() 
        
    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor


