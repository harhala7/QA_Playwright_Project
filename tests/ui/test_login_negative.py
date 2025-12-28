from playwright.sync_api import Page, expect
from tests.pages.login_page import LoginPage


def test_locked_out_user_cannot_login(page: Page, base_url: str):
    login = LoginPage(page, base_url)
    login.open()
    login.login_as("locked_out_user", "secret_sauce")

    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_contain_text("locked out")
