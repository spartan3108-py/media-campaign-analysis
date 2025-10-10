from fastapi import APIRouter, HTTPException
from src.conn.mongodb import campaigns_collection
from src.models.campaign import Campaign


router = APIRouter(
    prefix="/api/v1"
)


@router.post("/campaign", tags=["campaign"])
async def create_campaign(
        request: Campaign
):
    result = await campaigns_collection.insert_one(dict(request))
    return result.acknowledged

