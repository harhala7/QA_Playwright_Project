import pytest


@pytest.fixture(scope="session")
def browser_name():
    return "chromium"


@pytest.fixture(scope="session")
def headless():
    return True


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com"

from pathlib import Path
import pytest
from playwright.sync_api import Browser

STATE_PATH = Path("artifacts") / "storage_state.json"


@pytest.fixture
def authed_page(browser: Browser):
    if not STATE_PATH.exists():
        raise RuntimeError(
            "Brak artifacts/storage_state.json. "
            "Odpal najpierw: pytest -q tests/test_auth_setup.py"
        )

    context = browser.new_context(storage_state=str(STATE_PATH))
    page = context.new_page()
    yield page
    context.close()

