import os
import pytest
from sendrella import SendrellaClient

# Use env variable or fallback key (insert your actual key if not using env)
API_KEY = os.getenv("SENDRELLA_API_KEY", "93885cfb8501b017f8d508bf7b6e572de4e0489fa5d6ff96d17935c9a44ce8b3")

@pytest.fixture
def client():
    return SendrellaClient(api_key=API_KEY)

def test_get_credits(client):
    credits = client.utils.credits()
    
    # First assert the request was successful
    assert credits.get("success") is True, f"Unexpected response: {credits}"
    
    # Then check for expected fields
    assert "available_credits" in credits, "Missing 'available_credits' in credits response"
    assert "all_time_used" in credits
    assert "all_time_credits" in credits

def test_validate_key(client):
    result = client.utils.validate_key()
    
    assert "success" in result, "Missing 'success' key in validate_key response"
    assert result["success"] is True, f"Validation failed: {result}"
    assert "name" in result, "Missing 'name' in validate_key response"
