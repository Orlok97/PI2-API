from . import client, auth_token
from . import employee_payload as payload

def test_create_admin(client):
    response=client.post('/api/v1/admin/',json={"nome":"admin","email":"admin@admin.com","senha":"123"})
    assert response.status_code == 200
    print(response.get_json())