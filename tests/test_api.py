import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_simulate_endpoint_return_valid_response(client):
    payload = {
        "runs": 10,
        "bet": 5,
        "rounds_per_run": 3
    }

    response = client.post("/simulate", json=payload)

    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)

    assert "total_wins" in data
    assert "total_losses" in data
    assert "win_rate" in data
    assert "avg_profit" in data