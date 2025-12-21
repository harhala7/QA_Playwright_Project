from playwright.sync_api import Page, Locator


class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

        self.username: Locator = page.locator("[data-test='username']")
        self.password: Locator = page.locator("[data-test='password']")
        self.login_button: Locator = page.locator("[data-test='login-button']")

    def open(self) -> None:
        self.page.goto(self.base_url)

    def login_as(self, user: str, pwd: str) -> None:
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()
