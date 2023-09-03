from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# PostgreSQL configuration
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mysecretpassword@172.17.0.2:5432/todoapplicationdatabase"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()