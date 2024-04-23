from sqlalchemy import Column,Integer,String
from .database import Base
#from sqlalchemy.sql.sqltypes impo

class Student(Base):
    __tablename__="STUDENT"

    name=Column(String,primary_key=True,nullable=False)
    sclass=Column(String,nullable=False)
    section=Column(String,nullable=False)
