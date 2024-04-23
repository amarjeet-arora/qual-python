from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from .database import Base

class Student(Base):
    __tablename__="STUDENT"

    name=Column(String,primary_key=True,nullable=False)
    sclass=Column(String,nullable=False)
    section=Column(String,nullable=False)



---

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./mytest.db"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





from pydantic import BaseModel



class Student(BaseModel):
    name: str
    sclass: str
    section: str







from operator import index
from random import randrange
from fastapi import FastAPI, HTTPException, Response
from fastapi.params import Body
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi import status
import sqlite3
from . import models,schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)
 
app = FastAPI()

@app.get("/testconn")
def testdb(db: Session = Depends(get_db)):
    return {"status":"success"}

