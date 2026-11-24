"""Page Object for the Login page."""
import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # username field  -> id="id"
        self.username_input = page.locator("#id")
        # password field  -> id="pass"
        self.password_input = page.locator("#pass")
        # Login button: adjust if your app uses a different locator
        self.login_button = page.locator(
            "#login, button[type='submit'], input[type='submit']"
        ).first

    @allure.step("Enter username: {username}")
    def enter_username(self, username: str):
        self.fill(self.username_input, username, "username")

    @allure.step("Enter password")
    def enter_password(self, password: str):
        self.fill(self.password_input, password, "password")

    @allure.step("Click Login button")
    def click_login(self):
        self.click(self.login_button, "Login button")

    @allure.step("Login with user '{username}'")
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
