import pytest
from . import client, auth_token
from . import citizen_payload as payload
from . import employee_payload

def test_get_requests(client, auth_token):
    token=auth_token(payload)
    response=client.get('/api/v1/janitorial/',headers={'Authorization':f"Bearer {token}"})
    assert response.status_code == 200
    print(response.get_json())
    
def test_create_request(client, auth_token):
    token=auth_token(payload)
    data={
        "rua":"Rua Luis Gonçaves",
        "bairro":"JD Rio Branco",
        "area":"continental",
        "numero":"547",
        "cep":"11654789",
        "servico":"cata-treco",
        "desc":"descrição",
        "anexo":""
        }
    response=client.post('/api/v1/janitorial/',data=data, headers={'Authorization':f"Bearer {token}"})
    assert response.status_code == 200
    print(response.get_json())

def test_get_request_by_id(client, auth_token):
    token=auth_token(payload)
    response=client.get('/api/v1/janitorial/1', headers={'Authorization':f"Bearer {token}"})
    assert response.status_code == 200
    print(response.get_json())

def test_update_request(client, auth_token):
    token=auth_token(payload)
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
    response=client.put('/api/v1/janitorial/1',headers={'Authorization':f"Bearer {token}"}, json=payload)
    assert response.status_code == 200
    print(response.get_json())

def test_schedule_request(client, auth_token):
    token=auth_token(employee_payload)
    response=client.put('/api/v1/janitorial/schedule/1',headers={'Authorization':f'Bearer {token}'}, json={'data_prevista':'2025-05-14','status':'Finalizado'})
    assert response.status_code == 200
    print(response.get_json())

def test_delete_request(client, auth_token):
    token=auth_token(payload)
    response=client.delete('/api/v1/janitorial/1', headers={'Authorization':f"Bearer {token}"})
    assert response.status_code == 200
    print(response.get_json())