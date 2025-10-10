from motor.motor_asyncio import AsyncIOMotorClient
from src.settings import settings

client = AsyncIOMotorClient(settings.mongo_uri)
db = client[settings.db_name]

campaigns_collection = db["dummy-data"]
