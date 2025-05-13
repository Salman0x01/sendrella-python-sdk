# tests/test_temp_mail.py

import os
import pytest
from sendrella import SendrellaClient

API_KEY = os.getenv("SENDRELLA_API_KEY", "93885cfb8501b017f8d508bf7b6e572de4e0489fa5d6ff96d17935c9a44ce8b3")

@pytest.fixture
def client():
    return SendrellaClient(api_key=API_KEY)

def test_temp_check(client):
    result = client.temp_mail.check("user@mailinator.com")
    assert "is_disposable" in result

def test_temp_logs(client):
    logs = client.temp_mail.logs()
    assert "logs" in logs
    assert isinstance(logs["logs"], list)
