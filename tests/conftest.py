import pytest
import mongomock
from fastapi.testclient import TestClient
from io import StringIO
from dotenv import load_dotenv
from src.main import app
from src.conn.mongodb import MongoDBConns
from src.settings import SETTINGS

# Load dummy environment variables
envVar = """
MONGO_URI=dummy_uri
DB_NAME=test_db
"""
load_dotenv(stream=StringIO(envVar))


def mongo_data():
    """
    Provides a mocked MongoDB database for tests
    """
    mock_mongo_client = mongomock.MongoClient()
    mock_mongo_db = mock_mongo_client[SETTINGS.db_name]
    return mock_mongo_db


@pytest.fixture
def mock_mongo(mocker):
    """
    Fixture to patch MongoDBConns to use the mocked database
    """
    mock_db = mongo_data()
    # mongo_connection = MongoDBConns.__new__(MongoDBConns)  # create instance without __init__
    mongo_connection = MongoDBConns()
    mongo_connection.db = mock_db
    mongo_connection.client = None  # optional
    mock_db.create_collection("dummy-data")  # optional but safe

    # Patch MongoDBConns to always return this instance
    mocker.patch("src.conn.mongodb.MongoDBConns", return_value=mongo_connection)
    return mock_db


@pytest.fixture
def test_client():
    """
    FastAPI TestClient that uses patched MongoDBConns
    """
    with TestClient(app) as client:
        yield client
