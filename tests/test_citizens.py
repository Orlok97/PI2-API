from . import client

def test_create_citizen(client):
    payload={"nome":"Ana", "email":"ana@gmail.com","telefone":"13-45621435","senha":"123"}
    response=client.post('/api/v1/citizen/',json=payload)
    assert response.status_code == 200
    print(response.get_json())