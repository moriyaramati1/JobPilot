from http import HTTPStatus

from fastapi import APIRouter

from app.routes import HEALTH_ROUTE
from app.types.health import HealthStatusResponse

router = APIRouter()


@router.get(
    HEALTH_ROUTE,
    response_model=HealthStatusResponse,
    status_code=HTTPStatus.OK,
)
def get_health() -> HealthStatusResponse:
    return HealthStatusResponse(status="ok")
