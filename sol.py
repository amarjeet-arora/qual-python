@app.put("/updatepost/{id}")
def updatePost(id:int,post:Post):
    print(post)
    post=findPost2(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Given ID not found")
    post_dict=post.model_dump()
    post_dict['id'] =id
    my_post[index]=post_dict
    return {"data": post_dict}



from operator import index
