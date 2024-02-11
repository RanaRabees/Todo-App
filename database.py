# 1. Set up the PostgreSQL Database and SQLAlchemy Models
# database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session
import streamlit as st

# SQLALCHEMY_DATABASE_URL = st.secrets["SQLALCHEMY_DATABASE_URL"]
SQLALCHEMY_DATABASE_URL = "postgresql://RanaRabees:qi8nyaSBdJ7C@ep-black-pond-930754.us-east-2.aws.neon.tech/neondb?sslmode=require"

engine: Engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db: Session = Session()

class Base(DeclarativeBase):
    pass

class Todo(Base):
    """ Defines the todo model """
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    
    def __repr__(self) -> str:
        return f"<Todo {self.title}>"

Base.metadata.create_all(engine)    

db.commit()
print("Program Completed!")
