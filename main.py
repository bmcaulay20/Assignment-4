import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from backend.routers.players import router as players_router
from backend.routers.auth_routes import auth_router
from models.auth import get_current_user
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from database import users_collection
app = FastAPI(
    title="Basketball Stats",
    version="1.0.0",
    description="FastAPI backend with MongoDB, JWT auth, and bcrypt password hashing"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/login")
def serve_login():
    return FileResponse(os.path.join("frontend", "login.html"))

@app.get("/signup")
def serve_signup():
    return FileResponse(os.path.join("frontend", "signup.html"))

@app.get("/app")
def serve_app(user: dict = Depends(get_current_user)):
    return FileResponse(os.path.join("frontend", "index.html"))


@app.get("/")
async def home():
    return {"msg": "API is running"}




app.include_router(players_router)
app.include_router(auth_router)



app.mount("/frontend", StaticFiles(directory="frontend", html = True), name="frontend")
