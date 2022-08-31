import subprocess

import pytest


@pytest.fixture(scope="session", autouse=True)
def startup_localstack():
    subprocess.check_output(["localstack", "start", "-d"])
    subprocess.check_output(["localstack", "wait"])

    yield

    subprocess.check_output(["localstack", "stop"])
