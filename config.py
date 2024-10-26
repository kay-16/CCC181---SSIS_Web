from os import getenv
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
DB_NAME = getenv("DB_NAME")
DB_USERNAME = getenv("DB_USERNAME")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = int(getenv("DB_PORT", 3306))
BOOTSTRAP_SERVE_LOCAL = getenv("BOOTSTRAP_SERVE_LOCAL")

CLOUD_NAME = getenv("CLOUD_NAME")
CLOUD_KEY = getenv("CLOUD_KEY")
CLOUD_KEY_SECRET = getenv("CLOUD_KEY_SECRET")