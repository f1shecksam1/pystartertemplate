import logging

import pytest
from fastapi.testclient import TestClient

from pystartertemplate.main import app


@pytest.fixture()
def client() -> TestClient:
    logging.getLogger().setLevel(logging.WARNING)
    return TestClient(app)
