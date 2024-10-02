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


# Fetch the college according to the search parameters
def search_colleges(column, field):
    try:
        C = mysql.connection.cursor() 
        C.execute(f"SELECT * FROM college WHERE {column} COLLATE utf8mb4_bin LIKE '%{field}%';")
        return C.fetchall()
    
    except mysql.connection.Error as e:
        mysql.connection.rollback()  # In case of error
        raise e
    finally:
        C.close()  # Close the cursor


# Fetch college data based on college code
def get_college_by_code(col_code):
    C  = mysql.connection.cursor()
    try: 
        get_statement = """ SELECT * FROM college WHERE col_course_code = %s """
        
        C.execute(get_statement, (col_code,))

        results = C.fetchone()
        return results

    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor


# Updates college data
def edit_colleges(college):
    C  = mysql.connection.cursor()
    try:
        edit_statement = """
                        UPDATE college
                        SET col_course_code = %s, college_name = %s
                        WHERE col_course_code = %s;
                    """
        C.execute(edit_statement, college)
        mysql.connection.commit() 
        
    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor


# Removes college data based on college code
def delete_colleges(delete_college):
    C  = mysql.connection.cursor()
    try:
        delete_statement = """ DELETE FROM college WHERE col_course_code = %s; """

        C.execute(delete_statement, (delete_college,))
        mysql.connection.commit() 
        
    except Exception as e:
        mysql.connection.rollback()  # In case of error
        print(f"An error occurred: {e}")
    finally:
        C.close()  # Close the cursor
