from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/posts")
def get_posts():
    return {"data" : "These are your posts"}

@app.post("/createpost")
def create_post(new_post: Post):
    print(new_post.dict())
    return {"data": new_post}