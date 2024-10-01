from app import mysql

# Fetch all students from the database
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


