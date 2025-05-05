import pytest
from . import client, auth_token, admin_payload, employee_payload

def test_create_employee(client, auth_token):
    token=auth_token(admin_payload)
    payload={'nome':'Ana','email':'ana@gmail.com','senha':'123', 'cargo':'Dev'}
    response=client.post('/api/v1/employee/', headers={'Authorization':f'Bearer {token}'}, json=payload)
    assert response.status_code == 200
    print(response.get_json())

def test_list_employees(client,auth_token):
    token=auth_token(employee_payload)
    response=client.get('/api/v1/employee/',headers={'Authorization':f"Bearer {token}"})
    assert response.status_code == 200
    print(response.get_json())

def test_get_employee_by_id(client, auth_token):
    token=auth_token(employee_payload)
    response=client.get('/api/v1/employee/2',headers={'Authorization':f'Bearer {token}'})
    assert response.status_code == 200
    print(response.get_json())

def test_update_employee(client, auth_token):
    payload={'nome':'Ana Beatriz','email':'ana@gmail.com','senha':'123', 'cargo':'Dev'}
    token=auth_token(employee_payload)
    response=client.put('/api/v1/employee/2', headers={'Authorization':f'Bearer {token}'}, json=payload)
    assert response.status_code == 200
    print(response.get_json())

def test_delete_employee(client, auth_token):
    token=auth_token(employee_payload)
    response=client.delete('/api/v1/employee/2', headers={'Authorization':f'Bearer {token}'})
    assert response.status_code == 200
    print(response.get_json())