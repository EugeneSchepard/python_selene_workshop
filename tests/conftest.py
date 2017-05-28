import pytest
from testcontainers.compose import DockerCompose

@pytest.fixture(scope="session")
def setup(request):
    DockerCompose("/home/sergey/PycharmProjects/testing_stage/").start()
