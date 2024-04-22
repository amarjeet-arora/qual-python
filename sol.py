from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

#initialize the base data
my_post=[{"title":"demo app","content":"post-1","id":1}]
# initialize the fast API
app= FastAPI()

class Post(BaseModel):
    title:str
    content:str

@app.post("/adduser")
def create_post(newPost:Post):
   
    post_dict=newPost.dict()
    print(post_dict)
    post_dict['id']=randrange(0,10000000)
    my_post.append(post_dict)
    print(newPost)
    print(newPost.model_dump())
    return {"data":post_dict}

@app.get("/loadall")
def loadAll():
    return {"data": my_post}

