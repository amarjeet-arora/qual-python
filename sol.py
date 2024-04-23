from fastapi import FastAPI,status,Response,HTTPException
from fastapi.params import Body
from operator import index
from pydantic import BaseModel
from random import randrange


#initialize the base data
my_post=[{"title":"demo app","content":"post-1","id":1}]
# initialize the fast API
app= FastAPI()

class Post(BaseModel):
    title:str
    content:str
# add new record
@app.post("/adduser",status_code=status.HTTP_201_CREATED)
def create_post(newPost:Post):
   
    post_dict=newPost.dict()
    print(post_dict)
    post_dict['id']=randrange(0,10000000)
    my_post.append(post_dict)
    print(newPost)
    print(newPost.model_dump())
    return {"data":post_dict}
# load all the records
@app.get("/loadall")
def loadAll():
    return {"data": my_post}

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
@app.get("/loadpost/{uid}")
def loadByPostId(uid:int,response:Response):
    post=findPost(uid)
    if not post:
        response.status_code=status.HTTP_404_NOT_FOUND
        print(post)
        return {"Message":f"User not Found for :{uid}"}
    else:
        return {"data":post}

# search specific record
@app.get("/loadpost2/{uid}")
def loadByPostId(uid:int,response:Response):
    post=findPost(uid)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Given ID not found")
    else:
        return {"data":post}

@app.delete("/deletepost/{id}")
def deletePost(id:int):
    post=findPost2(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Given ID not found")
    else:
        my_post.pop(post)
        return {"Post deleted":post}

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


