from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Site is running 🔥"}

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <h1>🔥 Insta Growth Dashboard</h1>
    <p>Welcome to your system</p>
    """
