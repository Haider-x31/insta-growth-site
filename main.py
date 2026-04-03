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

    users[username] = {"points": 50}

    return f"""
    <h2>✅ Welcome {username}</h2>
    <p>Points: {users[username]['points']}</p>

    <form action="/order" method="post">
        <input type="hidden" name="username" value="{username}">
        <input name="link" placeholder="Instagram Link" required>
        <input name="amount" type="number" placeholder="Followers amount" required>
        <button type="submit">🚀 Send Order</button>
    </form>
    """

@app.post("/order", response_class=HTMLResponse)
def order(username: str = Form(...), link: str = Form(...), amount: int = Form(...)):
    
    if username not in users:
        return "<h2>❌ User not found</h2>"

    cost = amount * 2

    if users[username]["points"] < cost:
        return f"<h2>❌ Not enough points</h2><p>You have: {users[username]['points']}</p>"

    users[username]["points"] -= cost

    return f"""
    <h2>✅ Order Sent</h2>
    <p>Link: {link}</p>
    <p>Amount: {amount}</p>
    <p>Cost: {cost}</p>
    <p>Remaining Points: {users[username]['points']}</p>
    <a href="/">Back</a>
    """

@app.get("/users")
def get_users():
    return users
