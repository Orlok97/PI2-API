from . import client

def test_home_app(client):
    response=client.get('/')
    assert response.status_code == 200
    print(response.get_json())