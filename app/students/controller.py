from app import mysql

# Fetch all students from the database
def get_all_students():
    C = mysql.connection.cursor()
    try:
        C.execute("SELECT id_format, last_name, first_name, year_lvl, sex, stud_course_code FROM student ORDER BY last_name, first_name ASC;")
        rows = C.fetchall()
        print(rows) 
        return rows
    except Exception as e:
        print(f"An error occurred: {e}")
        return None # Return None or handle the error as needed
    finally:
        if C:   # Check if C is not None before closing
            C.close()   
    