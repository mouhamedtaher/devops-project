import pytest
from app import app

@pytest.fixture
def client():
    # On configure l'application en mode "Test"
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Vérifie que la racine / répond 200 OK"""
    response = client.get('/')
    assert response.status_code == 200

def test_health(client):
    """Vérifie que /health renvoie 'healthy'"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data