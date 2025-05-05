import pytest
from . import client, auth_token
from . import citizen_payload as payload

def test_create_citizen(client):
    payload={"nome":"João", "email":"joao@gmail.com","telefone":"13-2342341435","senha":"123"}
    response=client.post('/api/v1/citizen/',json=payload)
    assert response.status_code == 200
    print(response.get_json())

def test_list_citizens(client, auth_token):
    token=auth_token(payload)
    response=client.get('/api/v1/citizen/', headers={'Authorization':f"Bearer {token}"})
    assert response.status_code == 200
    print(response.get_json())

def test_get_citizen_by_id(client, auth_token):
    token=auth_token(payload)
    response=client.get('/api/v1/citizen/1',headers={'Authorization':f"Bearer {token}"})
    assert response.status_code == 200
    print(response.get_json())
    
def test_update_citizen(client, auth_token):
    data={"nome":"João Miguel","telefone":"(13) 9954542-7844","senha":"123"}
    token=auth_token(payload)
    response=client.put('/api/v1/citizen/1',headers={"Authorization":f"Bearer {token}"}, data=data)
    assert response.status_code == 200
    print(response.get_json())

def test_delete_citizen(client, auth_token):
    token=auth_token(payload)
    response=client.delete('/api/v1/citizen/1',headers={"Authorization":f"Bearer {token}"})
    assert response.status_code == 200
    print(response.get_json())