from flask import Flask
from config import SECRET_KEY, DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, BOOTSTRAP_SERVE_LOCAL
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

mysql = MySQL()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    # Load configurations
    app.config.from_object('config')
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['MYSQL_DB'] = DB_NAME
    app.config['MYSQL_USER'] = DB_USERNAME
    app.config['MYSQL_PASSWORD'] = DB_PASSWORD
    app.config['MYSQL_HOST'] = DB_HOST
    app.config['MYSQL_PORT'] = DB_PORT
    app.config['BOOTSTRAP_SERVE_LOCAL'] = BOOTSTRAP_SERVE_LOCAL
    app.config['MYSQL_DATABASE_SOCKET'] = ' '

    # Initialize extensions
    mysql.init_app(app)
    csrf.init_app(app)

    # Importing routes from all the packages
    from app.students.routes import students
    from app.programs.routes import programs
    from app.college.routes import college
    from app.login.routes import login
    from app.main.routes import main

    # Register blueprints
    app.register_blueprint(students)
    app.register_blueprint(programs)
    app.register_blueprint(college)
    app.register_blueprint(login)
    app.register_blueprint(main)

    return app
