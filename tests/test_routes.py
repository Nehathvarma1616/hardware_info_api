from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_cpu():
    response = client.get("/cpu/info")

    assert response.status_code == 200