from datetime import datetime, timezone
from typing import Any, Dict, Optional, Tuple

import certifi  # type: ignore
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError

from src.models.campaign import Campaign
from src.settings import SETTINGS


class MongoDBConns:
    """All connections, data exchange related to MongoDB"""

    def __init__(self):
        self.client = MongoClient(
            SETTINGS.mongo_uri,
            tlsCAFile=certifi.where(),
            server_api=ServerApi("1"),
        )
        self.db = self.client[SETTINGS.db_name]

    def close_connection(self) -> None:
        """
        Close MongoDB connection
        :returns None
        """
        self.client.close()

    def create_campaign(self, request: Campaign):
        try:
            campaign_data = {
                "name": request.name,
                "platform": request.platform,
                "status": request.status,
                "budget": request.budget,
                "created_at": datetime.now(timezone.utc),
                "updated_at": datetime.now(timezone.utc),
                "metadata": request.metadata,
            }
            coll = self.db.get_collection("dummy-data")
            result = coll.insert_one(campaign_data)
            print(f"Campaign created with ID: {result.inserted_id}")

            return str(result.inserted_id)

        except PyMongoError as e:
            print(f"Failed to create campaign: {e}")
            return False, str(e)
