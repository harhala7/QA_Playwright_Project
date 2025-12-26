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

def test_add_to_cart_shows_badge(page: Page, base_url: str):
    login = LoginPage(page, base_url)
    login.open()
    login.login_as("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()

    expect(inventory.cart_badge).to_have_text("1")

def test_add_to_cart_shows_badge_authed(authed_page, base_url: str):
    authed_page.goto(base_url + "/inventory.html")

    authed_page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    expect(authed_page.locator(".shopping_cart_badge")).to_have_text("1")

    import re
from playwright.sync_api import expect
from tests.pages.inventory_page import InventoryPage

def test_logout_redirects_to_login(authed_page, base_url: str):
    authed_page.goto(base_url + "/inventory.html")

    inventory = InventoryPage(authed_page)
    inventory.logout()

    expect(authed_page).to_have_url(re.compile(base_url + "/?$"))
    expect(authed_page.locator("[data-test='login-button']")).to_be_visible()

def test_sort_products_az(authed_page, base_url: str):
    authed_page.goto(base_url + "/inventory.html")

    inventory = InventoryPage(authed_page)
    inventory.sort_by("az")

    names = inventory.get_product_names()
    assert names == sorted(names)
