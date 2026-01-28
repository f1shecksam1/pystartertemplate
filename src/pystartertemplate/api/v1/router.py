from fastapi import APIRouter

from pystartertemplate.api.v1.echo import router as echo_router
from pystartertemplate.api.v1.health import router as health_router

router = APIRouter()

router.include_router(health_router)
router.include_router(echo_router)
