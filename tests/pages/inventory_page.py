from playwright.sync_api import Page, Locator


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.backpack_add: Locator = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_link: Locator = page.locator(".shopping_cart_link")
        self.cart_badge: Locator = page.locator(".shopping_cart_badge")
        self.menu_button: Locator = page.locator("#react-burger-menu-btn")
        self.logout_link: Locator = page.locator("[data-test='logout-sidebar-link']")
        self.sort_dropdown: Locator = page.locator("[data-test='product-sort-container']")
        self.item_names: Locator = page.locator(".inventory_item_name")

    def add_backpack_to_cart(self) -> None:
        self.backpack_add.click()

    def open_cart(self) -> None:
        self.cart_link.click()
        
    def logout(self) -> None:
        self.menu_button.click()
        self.logout_link.click()

    def sort_by(self, value: str) -> None:
    # SauceDemo values: az, za, lohi, hilo
        self.sort_dropdown.select_option(value)

    def get_product_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

