from . import client,  auth_token, admin_payload

def test_create_service(client, auth_token):
    token=auth_token(admin_payload)
    payload={'nome':'cata-treco', 'desc':'alguma descrição','prazo':3}
    response=client.post('/api/v1/service/',headers={'Authorization':f'Bearer {token}'},json=payload)
    assert response.status_code == 200
    print(response.get_json())

def test_list_services(client, auth_token):
    token=auth_token(admin_payload)
    response=client.get('/api/v1/service/',headers={'Authorization':f'Bearer {token}'})
    assert response.status_code == 200
    print(response.get_json())

def test_get_service_by_id(client, auth_token):
    token=auth_token(admin_payload)
    response=client.get('/api/v1/service/1',headers={'Authorization':f'Bearer {token}'})
    assert response.status_code == 200
    print(response.get_json())

def test_update_service(client, auth_token):
    token=auth_token(admin_payload)
    payload={'nome':'cata-treco', 'desc':'descrição editada','prazo':3}
    response=client.put('/api/v1/service/1',headers={'Authorization':f'Bearer {token}'}, json=payload)
    assert response.status_code == 200
    print(response.get_json())

def test_delete_service(client, auth_token):
    token=auth_token(admin_payload)
    response=client.delete('/api/v1/service/1',headers={'Authorization':f'Bearer {token}'})
    assert response.status_code == 200
    print(response.get_json())