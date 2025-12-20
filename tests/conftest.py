import pytest


@pytest.fixture(scope="session")
def browser_name():
    return "chromium"


@pytest.fixture(scope="session")
def headless():
    return True
