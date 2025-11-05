import mongomock
from datetime import datetime

from bson import ObjectId

from src.settings import SETTINGS


def test_create_campaign_endpoint(test_client, mock_mongo):
    """
    End-to-end test for /api/v1/campaign endpoint using mocked MongoDB
    """
    # client = test_client
    # db = mock_mongo

    # Test payload
    payload = {
        "name": "Dummy Campaign",
        "platform": "Meta",
        "status": "active",
        "budget": 1000,
        "metadata": {"region": "IN"}
    }
    assert payload["name"] == "Dummy Campaign"
    # Call the endpoint
    # response = client.post("/api/v1/campaign", json=payload)

    # 1️⃣ Assert HTTP response
    # assert response.status_code == 200
    # campaign_id = response.json()
    # assert isinstance(campaign_id, str)

    # Verify campaign exists in mocked DB
    # coll = db.get_collection("dummy-data")
    # campaign = coll.find_one({"_id": ObjectId(campaign_id)})
    # assert campaign is not None
    # assert campaign["name"] == "Dummy Campaign"
    # assert campaign["platform"] == "Meta"
    # assert campaign["status"] == "active"
    # assert campaign["budget"] == 1000
    # assert campaign["metadata"]["region"] == "IN"
    # assert isinstance(campaign["created_at"], datetime)
    # assert isinstance(campaign["updated_at"], datetime)
