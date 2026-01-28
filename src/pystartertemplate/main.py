from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from pystartertemplate.api import api_router
from pystartertemplate.core.config import settings
from pystartertemplate.core.logging import setup_logging

setup_logging(settings)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    logger.info("Application startup")
    app.state.settings = settings
    yield
    logger.info("Application shutdown")


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.project_name,
        version="0.1.0",
        debug=settings.debug,
        lifespan=lifespan,
    )

    app.include_router(api_router)

    @app.get("/", summary="Root endpoint")
    def root() -> dict[str, str]:
        logger.info("Root endpoint called")
        return {"message": "API is running"}

    return app


app = create_app()
