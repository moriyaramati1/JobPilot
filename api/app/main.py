from fastapi import FastAPI

from app.endpoints.health import router as health_router


def register_routers(app: FastAPI) -> None:
    app.include_router(health_router)


def create_app() -> FastAPI:
    app = FastAPI(title="JobPilot API")
    register_routers(app)
    return app


app = create_app()
