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
        return None # Return None or handle the error as needed
    finally:
        if C:   
            C.close()   # Close the cursor
        

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
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor


# Search students by all information
def search_students(query):
    C = mysql.connection.cursor()
    try:
        search_statement = """
                    SELECT * FROM student 
                    WHERE id_format LIKE %s 
                    OR CONCAT(first_name, ' ', last_name ) LIKE %s 
                    OR year_lvl LIKE %s 
                    OR sex = %s  
                    OR stud_course_code LIKE %s 
                """
        search_query = f"%{query}%"

        # Determine if the query is specifically 'male' or 'female'
        if query.lower() in ['male', 'female']:
             # Use the exact value for 'sex' and wildcards for other fields
            C.execute(search_statement, (search_query, search_query, search_query, query, search_query))
        else:
            # Apply wildcards everywhere if it's not a 'sex' search
            C.execute(search_statement, (search_query, search_query, search_query, None, search_query))

        results = C.fetchall()
        return results
    
    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
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
                        SET id_format = %s, first_name = %s, last_name = %s, year_lvl = %s, sex = %s, stud_course_code = %s 
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


