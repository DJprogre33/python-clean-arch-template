import logging

import uvicorn
from fastapi import FastAPI

from reflekt.config import ApiConfig


def create_app() -> FastAPI:
    app = FastAPI()
    return app


async def run_app(app: FastAPI, config: ApiConfig) -> None:
    server_config = uvicorn.Config(
        app=app,
        host=config.host,
        port=config.port,
        log_level=logging.INFO,
        log_config=None,
    )
    server = uvicorn.Server(config=server_config)
    await server.serve()
