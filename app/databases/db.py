import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import AppConfigSettings

SQLALCHEMY_DATABASE_URL = AppConfigSettings.POSTGRES_DATABASE_URL
if SQLALCHEMY_DATABASE_URL is None:
    from dotenv import load_dotenv
    load_dotenv()
    SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRES_DATABASE_URL")

print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
