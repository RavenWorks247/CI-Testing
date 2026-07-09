from app import app

client = app.test_client()


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_api():
    response = client.get("/api/message")
    assert response.status_code == 200
    assert response.json["message"] == "Hello from Backend!"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200