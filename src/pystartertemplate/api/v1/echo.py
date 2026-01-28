import logging

from fastapi import APIRouter

from pystartertemplate.models.echo import EchoIn, EchoOut
from pystartertemplate.services.echo_service import echo_text

router = APIRouter(prefix="/echo", tags=["echo"])
logger = logging.getLogger(__name__)


@router.post("", response_model=EchoOut)
def echo(payload: EchoIn) -> EchoOut:
    logger.info("Echo called with text=%r", payload.text)
    return echo_text(payload.text)
