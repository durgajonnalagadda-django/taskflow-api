from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# IMPORTANT: Change this to your MySQL username, password, db name
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:your_password@localhost/taskflow_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# This function will be used in main.py
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
