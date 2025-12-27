from pathlib import Path
from playwright.sync_api import Page, expect

ARTIFACTS_DIR = Path("artifacts")
STATE_PATH = ARTIFACTS_DIR / "storage_state.json"


def test_save_storage_state(page: Page, base_url: str):
    ARTIFACTS_DIR.mkdir(exist_ok=True)

    page.goto(base_url)
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    expect(page).to_have_url(base_url + "/inventory.html")

    page.context.storage_state(path=STATE_PATH)
