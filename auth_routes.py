from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from backend.database import users_collection
from models.user import UserCreate, Token
from core.hashpass import hash_password, verify_password, create_access_token

auth_router = APIRouter(prefix = "/auth", tags = ["auth"])

@auth_router.post("/register", status_code = status.HTTP_201_CREATED)
async def register(user: UserCreate):
    existing = await users_collection.find_one({"username" : user.username})
    if existing:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Username already exists")
    
    hashed = hash_password(user.password)
    await users_collection.insert_one({"username": user.username, "hashed_password":hashed})
    return{"msg": "User Registerd"}

@auth_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await users_collection.find_one({"username": form_data.username})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token}

