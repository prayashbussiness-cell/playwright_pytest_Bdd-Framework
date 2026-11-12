"""Page Object for the Dashboard page."""
import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def title_locator(self, title: str):
        # exact=True -> full, case-sensitive text match
        return self.page.get_by_text(title, exact=True)

    def username_locator(self, username: str):
        return self.page.get_by_text(username, exact=True)

    @allure.step("Verify dashboard title '{title}' is visible")
    def verify_title(self, title: str):
        self.log.info("Verifying dashboard title: %s", title)
        expect(self.title_locator(title).first).to_be_visible()

    def is_title_visible(self, title: str) -> bool:
        return self.title_locator(title).first.is_visible()

    @allure.step("Verify username '{username}' is shown on dashboard")
    def verify_username(self, username: str):
        self.log.info("Verifying dashboard username: %s", username)
        expect(self.username_locator(username).first).to_be_visible()
