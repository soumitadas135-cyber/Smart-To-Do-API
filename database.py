from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = AsyncIOMotorClient(MONGO_URI)
db = client.smart_todo

# ✅ Define collection HERE
users_collection = db.users


# ✅ Define helper function
async def get_user_by_username(username: str):
    return await users_collection.find_one({"username": username})