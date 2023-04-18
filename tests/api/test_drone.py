from entry import app
from fastapi.testclient import TestClient


def test_read_data_for_new_task():
    with TestClient(app=app) as client:
        response = client.get(
            '/station/new_task/'
        )
        resp_data = response.json()
        assert response.status_code == 200
        assert resp_data["id"] == 2
        assert resp_data["latitude"] == 10.1
        assert resp_data["longitude"] == 20.2


def test_add_task_to_db():
    with TestClient(app=app) as client:
        latitude: float = 99.9
        longitude: float = 88.9
        priority: str = "VIP"
        json_data = {
            "latitude": latitude,
            "longitude": longitude,
            "priority": priority
        }
        response = client.post(
            '/station/add_coord',
            json=json_data
        )
        assert response.status_code == 200
        resp_data = response.json()
        assert resp_data["latitude"] == latitude
        assert resp_data["longitude"] == longitude


def test_add_dron_status():
    with TestClient(app=app) as client:
        drone_id: int = 1
        battery: int = 12
        d_latitude: float = 10.10
        d_longitude: float = 20.20
        json_data = {
            "drone_id": drone_id,
            "battery": battery,
            "d_latitude": d_latitude,
            "d_longitude": d_longitude
        }
        response = client.post(
            '/drone/add_drone_info',
            json=json_data
        )
        assert response.status_code == 200
        resp_data = response.json()
        assert resp_data["latitude"] == d_latitude
        assert resp_data["longitude"] == d_longitude
