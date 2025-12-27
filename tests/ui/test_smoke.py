import re
from playwright.sync_api import Page, expect
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage



def test_homepage_has_title(page: Page, base_url: str):
    page.goto(base_url)
    expect(page).to_have_title(re.compile("Swag Labs"))


def test_login_happy_path_shows_inventory(page: Page, base_url: str):
    login = LoginPage(page, base_url)
    login.open()
    login.login_as("standard_user", "secret_sauce")

    expect(page).to_have_url(re.compile(".*/inventory.html"))
    expect(page.locator(".inventory_list")).to_be_visible()

