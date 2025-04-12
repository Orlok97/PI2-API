import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_token(client):
    payload={"email":"joao@gmail.com", "senha":"123", "permission":"citizen"}
    response=client.post('/api/v1/auth/',json=payload)
    assert response.status_code == 200
    return response.get_json()['token']