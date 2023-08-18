from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:

    app = FastAPI(
        title="User Service API",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_headers=["*"],
    )

    # include all routes here
    from app.v1 import v1_router

    app.include_router(v1_router)

    return app
