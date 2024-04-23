from operator import index
from random import randrange
from fastapi import FastAPI, HTTPException, Response
from fastapi.params import Body
from pydantic import BaseModel
from fastapi import status
import sqlite3

my_post=[{"title":"demo app","content":"post-1","id":1}]

app = FastAPI()

connection_obj = sqlite3.connect('mytest.db', check_same_thread=False)
cursor_obj = connection_obj.cursor()


def findPost(id):
    for p in my_post:
        if p['id'] == id:
            return p


def findPost2(id):
    for i, p in enumerate(my_post):
        if p['id'] == id:
            return i


print("connected to DB")


class Post(BaseModel):
    name: str
    sclass: str
    section: str


@app.post("/adduser", status_code=status.HTTP_201_CREATED)
def createPost(newPost: Post):

   # print(newPost)
    cursor_obj.execute(" " "INSERT INTO STUDENT(NAME,CLASS,SECTION) VALUES (?, ?, ?) RETURNING * " " ", (
        newPost.name, newPost.sclass, newPost.section
    ))

    np = cursor_obj.fetchone()
    connection_obj.commit()
    return {"data": np}


# load all the records
@app.get("/loadall")
def loadAll():
    cursor_obj.execute('''SELECT * FROM STUDENT''')
    my_post2=cursor_obj.fetchall()
    return {"data": my_post2}

# helper function

def findPost(id):
    for p in my_post:
        if p['id'] == id:
            return p

def findPost2(id):
    for i, p in enumerate(my_post):
        if p['id'] == id:
            return i


# search specific record
@app.get("/loadpost/{name}")
def loadByPostId(name: str):
    cursor_obj.execute(
        " " "select * from student where name=? " " ",(str(name),))
    test_post= cursor_obj.fetchone()
    print(test_post)

    if not test_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Given Name not found")
    else:
        return {"data":test_post}



@app.delete("/deletepost/{name}")
def deletePost(name:str):
    cursor_obj.execute(
        " " "delete from student where name=? " " ",(str(name),))
    deleted_post= cursor_obj.fetchone()
    connection_obj.commit()
    if not deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Given ID not found")
    else:
        return ("Post deleted")





@app.put("/updatepost/{id}")
def updatePost(id:int,post:Post):
    print(post)
    index=findPost2(id)
    if index == None:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Given ID not found")
    post_dict=post.model_dump()
    post_dict['id'] =id
    my_post[index]=post_dict
    return {"data": post_dict}


