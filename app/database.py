import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()
##loading the databse url
DATABASE_URL=os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("the specified path is not valid")


# communication between database connection manager

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Generates a python base class(Base).Any database model
# table class you create later will inherit from base so
# SQLAlchemy can map it to database tables

Base=declarative_base()


def get_db():
    # open a new database session
    db= SessionLocal()

    try:
        yield db
    finally:
        db.close()