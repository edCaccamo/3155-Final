import pytest
from fastapi.testclient import TestClient
from api.core.app import app

client = TestClient(app)

def test_create_recipe():
    payload = {
        "sandwich_id": 1,
        "resources": [
            {"resource_id": 1, "amount": 2},
            {"resource_id": 2, "amount": 3}
        ]
    }

    response = client.post("/recipes", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["sandwich_id"] == 1