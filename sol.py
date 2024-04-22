
from fastapi import FastAPI
from fastapi.params import Body
# initialize the fast API
app= FastAPI()
# initialize the get function
@app.get("/")
def root():
    return {"message":"welcome to FAST APPLICATION "}

@app.get("/user")
def messageShow():
    return {"message":"welcome to FAST APP "}
@app.post("/createposts")
def create_posts(data: dict=Body(...)):
    print(data)
    return {"message":"User created"}
