"""BasePage: common wrappers (with logging + Allure steps) used by all pages."""
import allure
from playwright.sync_api import Page

from utils.logger import get_logger


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.log = get_logger(self.__class__.__name__)

    @allure.step("Open URL: {url}")
    def open(self, url: str):
        self.log.info("Navigating to %s", url)
        self.page.goto(url)

    def fill(self, locator, value: str, name: str = "field"):
        self.log.info("Typing into %s", name)
        locator.fill(value)

    def click(self, locator, name: str = "element"):
        self.log.info("Clicking %s", name)
        locator.click()
