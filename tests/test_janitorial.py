import pytest
from . import client, auth_token

def test_get_requests(client, auth_token):
    response=client.get('/api/v1/janitorial/',headers={'Authorization':f"Bearer {auth_token}"})
    assert response.status_code == 200
    print(response.get_json())
    
def test_create_request(client, auth_token):
    payload={
        "rua":"Rua Luis Gonçaves",
        "bairro":"JD Rio Branco",
        "area":"continental",
        "numero":"547",
        "cep":"11654789",
        "servico":"cata-treco",
        "desc":"descrição",
        "anexo":""
        }
    response=client.post('/api/v1/janitorial/',data=payload, headers={'Authorization':f"Bearer {auth_token}"})
    assert response.status_code == 200
    print(response.get_json())

def test_get_request_by_id(client, auth_token):
    response=client.get('/api/v1/janitorial/1', headers={'Authorization':f"Bearer {auth_token}"})
    assert response.status_code == 200
    print(response.get_json())

def test_update_request(client, auth_token):
    payload={
        "rua":"Rua Ferndado Salles",
        "bairro":"JD Rio Humatá",
        "area":"continental",
        "numero":"555",
        "cep":"1167894",
        "servico":"cata-treco",
        "desc":"alguma descrição",
        "anexo":None
    }
    response=client.put('/api/v1/janitorial/1',headers={'Authorization':f"Bearer {auth_token}"}, json=payload)
    assert response.status_code == 200
    print(response.get_json())

def test_delete_request(client, auth_token):
    response=client.delete('/api/v1/janitorial/1', headers={'Authorization':f"Bearer {auth_token}"})
    assert response.status_code == 200
    print(response.get_json())