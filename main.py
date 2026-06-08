from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/posts")
def get_posts():
    return {"data" : "These are your posts"}

@app.post("/createpost")
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {"New Post": f"Title: {payLoad['title']} content: {payLoad['content']}"}
