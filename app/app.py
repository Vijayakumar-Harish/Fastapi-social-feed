from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "cool test post"},
    2: {"title": "Daily Update", "content": "just sharing some cool stuff"},
    3: {"title": "Hello World", "content": "testing another random post"},
    4: {"title": "Quick Thought", "content": "consistency beats motivation"},
    5: {"title": "Coding Vibes", "content": "writing some fun python scripts"},
    6: {"title": "Inspiration Hit", "content": "dream big, start small"},
    7: {"title": "Night Mode", "content": "late night creativity kicks in"},
    8: {"title": "Coffee Break", "content": "fueling my ideas today"},
    9: {"title": "Learning Daily", "content": "progress is progress"},
    10: {"title": "Chill Post", "content": "relaxing and thinking"},
    11: {"title": "Productive Day", "content": "getting things done feels great"},
}


@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title":post.title, "content":post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post

