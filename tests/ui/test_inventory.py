import re
from playwright.sync_api import Page, expect
from tests.pages.inventory_page import InventoryPage



def test_add_to_cart_shows_badge(authed_page, base_url: str):
    authed_page.goto(base_url + "/inventory.html")

    inventory = InventoryPage(authed_page)
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
