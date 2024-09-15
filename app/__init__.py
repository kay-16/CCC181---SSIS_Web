from flask import Flask
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from flask_wtf.csrf import CSRFProtect


mysql = MySQL()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DB=DB_NAME,
        MYSQL_HOST=DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )

    # register blueprints
    from app.students import student_bp
    app.register_blueprint(student_bp, url_prefix="/student")

    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    
    return app

