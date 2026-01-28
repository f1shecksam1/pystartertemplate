from fastapi.testclient import TestClient


def test_echo_ok(client: TestClient) -> None:
    response = client.post("/api/v1/echo", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json() == {"echoed": "hello"}


def test_echo_validation_error(client: TestClient) -> None:
    response = client.post("/api/v1/echo", json={})
    assert response.status_code == 422
