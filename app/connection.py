from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

from app.config import settings

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{settings.database_username}:%s@{settings.database_hostname}:{settings.database_port}/{settings.database_name}" % quote_plus(str(settings.database_password))

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
