import re
from playwright.sync_api import Page, expect


def test_homepage_has_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title(re.compile("Swag Labs"))


def test_login_happy_path_shows_inventory(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    expect(page).to_have_url(re.compile(".*/inventory.html"))
    expect(page.locator(".inventory_list")).to_be_visible()
