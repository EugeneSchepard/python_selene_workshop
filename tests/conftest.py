import os

import pytest
from testcontainers.compose import DockerCompose


@pytest.fixture(scope="session")
def setup(request):
    compose = DockerCompose(os.path.join(os.path.dirname(__file__), ".."))
    compose.start()
    compose.wait_for("http://localhost:8086")
