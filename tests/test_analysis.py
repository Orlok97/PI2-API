import pytest
from app import app, db
from database.models import Janitorial, Analysis

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()

            # Cria 12 registros para simular a lógica
            for i in range(12):
                j = Janitorial(
                    user_id=f"user_{i}",
                    user_name=f"Usuário {i}",
                    bairro="Centro",
                    cep="11750-000"
                )
                db.session.add(j)
                db.session.commit()

                a = Analysis(
                    janitorial_id=j.id,
                    data_solicitacao="2024-01-01",
                    data_finalizado="2024-01-02",
                    hora_solicitacao="08:00",
                    hora_finalizado="09:00"
                )
                db.session.add(a)

            db.session.commit()
        yield client

def test_analysis_route_returns_data(client):
    response = client.get('/api/v1/analysis/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 10 
