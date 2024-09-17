from app import mysql
import mysql.connector as mysql

# Fetch all students from the database
def get_all_students():
    try:
        C = mysql.connection.cursor()
        C.execute("SELECT * FROM `student` ORDER BY 'id_format', 'last_name', 'first_name' ASC;")
        rows = C.fetchall()
        for row in rows:
            print(row)
    finally:
        C.close()
    