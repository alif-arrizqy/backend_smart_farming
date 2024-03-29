from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.base import api_router


def include_router(app):
    app.include_router(api_router)


def start_app():
    app = FastAPI()
    origins = [
        "http://localhost:5100",
        "http://127.0.0.1:5100",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "http://192.168.0.102:8080",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    include_router(app)
    return app

app = start_app()
