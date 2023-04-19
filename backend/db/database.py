from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB = None

if 'DATABASE_URL' not in os.environ:
    DB = "postgresql://postgres:postgrespw@localhost:32768"
else:
    DB = os.environ['DATABASE_URL']

SQLALCHEMY_DATABASE_URL = DB

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()