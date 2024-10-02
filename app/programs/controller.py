from app import mysql

# Fetch all programs from the database
def get_programs():
    C = mysql.connection.cursor()
    try:
        C.execute("SELECT * FROM program ORDER BY course_code ASC;")
        rows = C.fetchall()
        return rows
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None # Handle the error as needed
    finally:
        if C:   
            C.close()   # Close the cursor


# Fetch all colleges from the database
def get_college():
    C = mysql.connection.cursor()
    try:
        C.execute("SELECT col_course_code, college_name FROM college ORDER BY col_course_code ASC;")
        rows = C.fetchall()
        return rows

    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # Handle the error as needed
    finally:
        if C:
            C.close()


# Adds the program to the database
def add_program_to_db(program):
    C = mysql.connection.cursor()
    try:
        add_statement = """
            INSERT INTO program (course_code, course_name, college_belong)
            VALUES (%s, %s, %s);
        """
        C.execute(add_statement, program)
        mysql.connection.commit()

    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()   # Close the cursor


# Fetch the program according to the search parameters
def search_programs(column, field):
    try:
        C = mysql.connection.cursor() 
        C.execute(f"SELECT * FROM program WHERE {column} COLLATE utf8mb4_bin LIKE '%{field}%';")
        return C.fetchall()
    
    except mysql.connection.Error as e:
        mysql.connection.rollback()  # In case of error
        raise e
    finally:
        C.close()  # Close the cursor


# Checks for duplicated ID
def check_course_code_exists(c_code):
    C = mysql.connection.cursor()
    try:
        C.execute("""SELECT EXISTS(SELECT 1 FROM program WHERE course_code = %s);""", (c_code,))
        exists = C.fetchone()[0] > 0
        return exists
     
    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close() # Close the cursor


# Fetch student data based on ID
def get_program_by_code(c_code):
    C  = mysql.connection.cursor()
    try: 
        get_statement = """ SELECT * FROM program WHERE course_code = %s """
        
        C.execute(get_statement, (c_code,))

        results = C.fetchone()
        return results

    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor


# Updates program data
def edit_programs(program):
    C  = mysql.connection.cursor()
    try:
        edit_statement = """
                        UPDATE program
                        SET course_code = %s, course_name = %s, college_belong = %s 
                        WHERE course_code = %s;
                    """
        C.execute(edit_statement, program)
        mysql.connection.commit() 
        
    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor


# Removes program data based on course code
def delete_programs(program_code):
    C  = mysql.connection.cursor()
    try:
        delete_statement = """ DELETE FROM program WHERE course_code = %s; """

        C.execute(delete_statement, (program_code,))
        mysql.connection.commit() 
        
    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor

