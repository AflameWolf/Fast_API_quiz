from sqlalchemy import create_engine
import os
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:5432/root")





