# tests/test_bounce.py

import os
import pytest
from sendrella import SendrellaClient

API_KEY = os.getenv("SENDRELLA_API_KEY", "93885cfb8501b017f8d508bf7b6e572de4e0489fa5d6ff96d17935c9a44ce8b3")

@pytest.fixture
def client():
    return SendrellaClient(api_key=API_KEY)

def test_bounce_check(client):
    response = client.bounce.check("hello@example.com")
    assert isinstance(response, dict)
    assert "status" in response

def test_bounce_logs(client):
    response = client.bounce.logs()
    assert "logs" in response
    assert isinstance(response["logs"], list)
