import pytest
from . import client

def test_create_citizen(client):
    payload={"nome":"João", "email":"joao@gmail.com","telefone":"13-2342341435","senha":"123"}
    response=client.post('/api/v1/citizen/',json=payload)
    assert response.status_code == 200
    print(response.get_json())

@pytest.fixture
def auth_token(client):
    payload={"email":"ana@gmail.com", "senha":"123", "permission":"citizen"}
    response=client.post('/api/v1/auth/',json=payload)
    assert response.status_code == 200
    return response.get_json()['token']

def test_list_citizens(client, auth_token):
    response=client.get('/api/v1/citizen/', headers={'Authorization':f"Bearer {auth_token}"})
    assert response.status_code == 200
    print(response.get_json())

def test_get_citizen_by_id(client, auth_token):
    response=client.get('/api/v1/citizen/4',headers={'Authorization':f"Bearer {auth_token}"})
    assert response.status_code == 200
    print(response.get_json())
    
def test_update_citizen(client, auth_token):
    payload={"nome":"Ana Maria","telefone":"(13) 9954542-7844","senha":"123"}
    response=client.put('/api/v1/citizen/3',headers={"Authorization":f"Bearer {auth_token}"}, data=payload)
    assert response.status_code == 200
    print(response.get_json())

def test_delete_citizen(client, auth_token):
    response=client.delete('/api/v1/citizen/1',headers={"Authorization":f"Bearer {auth_token}"})
    assert response.status_code == 200
    print(response.get_json())