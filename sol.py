from operator import index
from random import randrange
from fastapi import FastAPI, HTTPException, Response, Depends
from fastapi.params import Body
from sqlalchemy.orm import Session
from fastapi import status
import sqlite3
import models,schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.get("/testconn")
def loadAll(db: Session = Depends(get_db)):
    return {"status": "success"}


@app.post("/adduser", status_code=status.HTTP_201_CREATED)
def createPost(student:schemas.Student,db:Session=Depends(get_db)):
    #new_post=models.Student(name=student.name,sclass=student.sclass,section=student.section)
    new_post=models.Student(**student.dict())
    print(new_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data added": new_post}
