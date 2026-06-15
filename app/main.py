from typing import Optional
from fastapi import FastAPI, Response , status , HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from psycopg2.extras import RealDictCursor
import time

models.Base.metadata.create_all(bind = engine)
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
                                password='Aadi9654@', cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database Connection Successfull")
        break
    except Exception as error:
        print("Connection to Database Failed!")
        print("Error: ", error)
        time.sleep(2)


my_post = [{"title":"Title of Post 1", "content":"Content of Post 1", "id": 1},{"title":"Favourite Foods", "content":"I Like Chicken", "id": 2}]

def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p
        
def find_index(id):
    for i, p in enumerate(my_post):
        if p["id"] == id:
            return i
         
@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    return {"status" : "Success"}

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # post = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {"data" : posts}

@app.post("/createpost", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = models.Post(title=post.title, content = post.content , published = post.published)
    return {"data " :new_post}

@app.get("/posts/latest")
def latest_post():
    post = my_post[len(my_post)-1]
    return {"detals": post}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{f"post with id: {id} not found"}
    return {"data": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def del_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id),))
    del_post = cursor.fetchone()
    conn.commit()
    if del_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",(post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return{"data": updated_post}