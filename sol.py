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

@app.get("/loadall")
def loadAll(db:Session=Depends(get_db)):
    posts=db.query(models.Student).all()
    print(posts)
    return {"data":posts}

@app.get("/loadpost/{name}")
def loadByPostId(name: str,db:Session=Depends(get_db)):
    post=db.query(models.Student).filter(models.Student.name == name).first()
    print(post)
    return {"data": post}


@app.delete("/deletepost/{name}")
def deletePost(name:str,db:Session=Depends(get_db)):
    post=db.query(models.Student).filter(models.Student.name == name)
    if post.first() ==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Given ID not found")
    post.delete(synchronize_session=False)
    db.commit()
    
    return {"data": "User deleted"}

@app.put("/updatepost/{name}")
def updatePost(name:str,newstudent:schemas.Student,db:Session=Depends(get_db)):
    updated_post=db.query(models.Student).filter(models.Student.name == name)
    student=updated_post.first()
    if student ==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Given ID not found")
    updated_post.update(newstudent.dict(),synchronize_session=False)
    db.commit()
    return {"data":updated_post.first()}



