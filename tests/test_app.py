from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestApp:

    def test_hello(self):
        response = client.get("/hello")
        assert response.status_code == 200

    def test_status(self):
        response = client.get("/status")
        assert response.status_code == 200
        assert response.json()['status'] == 401
