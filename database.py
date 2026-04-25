from motor.motor_asyncio import AsyncIOMotorClient
from backend.core.config import settings

client = AsyncIOMotorClient(settings.MONGO_URL)
db = client[settings.DB_NAME]

players_collection = db["players"]
users_collection = db["users"]
