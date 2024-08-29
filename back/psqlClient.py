from config import DB_PORT, DB_USER, DB_HOST, DB_NAME, DB_PASS
import sqlalchemy as sqla

engine = sqla.create_engine("sqlite:///european_database.sqlite")

conn = engine.connect()