from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

posts : list[dict] = [
    {
        "id" : 1,
        "author" :  "corey schafer" ,
        "title" : "Fastapi is Awesome",
        "content" : "this framework is really easy to use and fast",
        "date posted" : "April 20 , 2025",
    },
    {
        "id" : 2,
        "author" :  "Jane Doe" ,
        "title" : "Python is greate for web development",
        "content" : "Python is greate for web development and fastapi make it even better",
        "date posted" : "April 21 , 2025",
    }
]
@app.get("/" , response_class=HTMLResponse , include_in_schema=False)
@app.get("/posts" , response_class=HTMLResponse , include_in_schema=False)
def root():
    return f"<h1> Hello world </h1>"

@app.get("/api/posts" , response_class=HTMLResponse)
def get_posts():
    return f"<h2> {posts}</h2>"


@app.post("/api/post/:id")
def post():
    return posts

