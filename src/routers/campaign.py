from fastapi import APIRouter, HTTPException
from src.conn.mongodb import MongoDBConns
from src.models.campaign import Campaign


router = APIRouter(
    prefix="/api/v1"
)


@router.post("/campaign", tags=["campaign"])
async def create_campaign(
        request: Campaign
):
    mongo_conn = MongoDBConns()
    result = mongo_conn.create_campaign(request)
    return result

