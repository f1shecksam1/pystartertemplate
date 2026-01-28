import logging

from fastapi import APIRouter

from pystartertemplate.models.health import HealthOut
from pystartertemplate.services.health_service import get_health_status

router = APIRouter(prefix="/health", tags=["health"])
logger = logging.getLogger(__name__)


@router.get("", response_model=HealthOut)
def health() -> HealthOut:
    logger.info("Health endpoint called")
    return get_health_status()
