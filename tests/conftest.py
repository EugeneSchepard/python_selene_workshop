import os

import pytest
from testcontainers.compose import DockerCompose


@pytest.fixture(scope="session")
def setup(request):
    DockerCompose(os.path.join(os.path.dirname(__file__), "..")).start()
