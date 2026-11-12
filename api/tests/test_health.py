from http import HTTPStatus

from fastapi.testclient import TestClient

from app.routes import HEALTH_ROUTE


def test_get_health_returns_ok(client: TestClient) -> None:
    response = client.get(HEALTH_ROUTE)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"status": "ok"}
