from fastapi import APIRouter, HTTPException
from app.auth import hash_password, verify_password, create_token
from app.database import users_collection, get_user_by_username

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register")
async def register(user: dict):
    username = user["username"].strip()

    # Check if user exists
    existing = await users_collection.find_one({"username": username})
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user["username"] = username
    user["password"] = hash_password(user["password"])

    await users_collection.insert_one(user)
    return {"message": "User registered successfully"}


@router.post("/login")   # ✅ FIXED PATH
async def login(user: dict):   # ✅ FIXED async
    db_user = await get_user_by_username(user["username"])  # ✅ await works now

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user["password"], db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": db_user["username"]})

    return {
        "access_token": token,
        "token_type": "bearer"
    }