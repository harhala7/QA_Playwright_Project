from playwright.sync_api import Page, Locator


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.backpack_add: Locator = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_link: Locator = page.locator(".shopping_cart_link")
        self.cart_badge: Locator = page.locator(".shopping_cart_badge")

    def add_backpack_to_cart(self) -> None:
        self.backpack_add.click()

    def open_cart(self) -> None:
        self.cart_link.click()
