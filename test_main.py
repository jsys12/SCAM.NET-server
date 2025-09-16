from fastapi.testclient import TestClient
from main import app  # Импорт твоего app из main.py

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
