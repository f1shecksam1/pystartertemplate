import logging

import pytest
from fastapi.testclient import TestClient

from pystartertemplate.main import app


@pytest.fixture()
def client() -> TestClient:
    logging.getLogger().setLevel(logging.INFO)
    return TestClient(app)
