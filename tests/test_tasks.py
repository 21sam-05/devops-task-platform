from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "DevOps Task Platform is running!"
    }


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.json()

    assert "tasks" in data
    assert len(data["tasks"]) == 2