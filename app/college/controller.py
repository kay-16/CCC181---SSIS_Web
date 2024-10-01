from app import mysql

# Fetch all colleges from the database
def get_all_college():
    C = mysql.connection.cursor()
    try:
        C.execute("SELECT col_course_code, college_name FROM college ORDER BY col_course_code ASC;")
        rows = C.fetchall()
        return rows
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None # Handle the error as needed
    finally:
        if C:   
            C.close()   # Close the cursor


# Adds the college to the database
def add_college_to_db(college):
    C = mysql.connection.cursor()
    try:
        insert_statement = """
            INSERT INTO college (col_course_code, college_name) 
            VALUES (%s, %s);
        """
        C.execute(insert_statement, college)
        mysql.connection.commit()

    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor


# Checks for duplicated college code
def check_college_code_exists(col_code):
    C = mysql.connection.cursor()
    try:
        C.execute("""SELECT EXISTS(SELECT 1 FROM college WHERE col_course_code = %s);""", (col_code,))
        exists = C.fetchone()[0] > 0
        return exists
     
    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close() # Close the cursor
