
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
# initialize the fast API
app= FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool = True

# initialize the get function
@app.get("/")
def root():
    return {"message":"welcome to FAST APPLICATION "}

@app.get("/user")
def messageShow():
    return {"message":"welcome to FAST APP "}
@app.post("/createposts")
def create_posts(payload: Post):
    print(payload)
    return {"data": "newpost"}
   # return {"New_User":f"title {payload['uname']} password : {payload['password']}"}
