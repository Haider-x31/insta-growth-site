from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

users = {}

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>🔥 Insta Growth</h1>
    <form action="/register" method="post">
        <input name="username" placeholder="Username" required>
        <button type="submit">Register</button>
    </form>
    """

@app.post("/register", response_class=HTMLResponse)
def register(username: str = Form(...)):
    if username in users:
        return f"<h2>❌ Username already exists</h2>"
    
    users[username] = {"points": 10}
    
    return f"""
    <h2>✅ Welcome {username}</h2>
    <p>Points: {users[username]['points']}</p>
    <a href='/'>Back</a>
    """

@app.get("/users")
def get_users():
    return users
