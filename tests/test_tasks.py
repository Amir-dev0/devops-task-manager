from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "DevOps Task Manager is running"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn Docker",
            "description": "Containerize the application",
            "priority": "medium",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Learn Docker"
    assert data["priority"] == "medium"
    assert data["completed"] is False
    assert "id" in data


def test_create_invalid_task():
    response = client.post(
        "/tasks",
        json={
            "title": "",
            "description": "Invalid task",
            "priority": "banana",
        },
    )

    assert response.status_code == 422