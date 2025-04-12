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
