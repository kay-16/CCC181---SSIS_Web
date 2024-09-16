from flask import Flask

app = Flask(__name__)

# Importing routes from all the packages
from app.app import app                 
from app.students.routes import students
from app.programs.routes import programs
from app.college.routes import college
from app.register.routes import register
from app.login.routes import login
from app.main.routes import main

app.register_blueprint(students)
app.register_blueprint(programs)
app.register_blueprint(college)
app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(main)