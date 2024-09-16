from flask import Flask

app = Flask(__name__)

from app.app import app  # Importing your routes from app.py here
