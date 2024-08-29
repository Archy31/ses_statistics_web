from dotenv import load_dotenv as __load_dotenv
import os as __os

__load_dotenv()

DB_HOST = __os.environ.get("DB_HOST")
DB_PORT = __os.environ.get("DB_PORT")
DB_NAME = __os.environ.get("DB_NAME")
DB_USER = __os.environ.get("DB_USER")
DB_PASS = __os.environ.get("DB_PASS")