from dotenv import load_dotenv as __load_dotenv
import os as __os

__load_dotenv()


HOST = __os.environ.get("HOST")
PORT = __os.environ.get("PORT")