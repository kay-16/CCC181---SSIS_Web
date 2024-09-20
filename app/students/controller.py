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

