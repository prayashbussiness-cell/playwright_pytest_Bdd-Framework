"""Step definitions (pytest-bdd) for login.feature."""
import allure
import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.config import Config
from utils.screenshot_util import take_screenshot

scenarios("login.feature")


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)


@given("the user is on the login page")
def open_login_page(login_page):
    login_page.open(Config.BASE_URL)


@when(parsers.parse('the user logs in with username "{username}" and password "{password}"'))
def do_login(login_page, username, password):
    login_page.login(username, password)


@then("a screenshot of the page after login is captured")
def screenshot_after_login(page):
    page.wait_for_load_state("networkidle")
    take_screenshot(page, "after_login_dashboard")


@then(parsers.parse('the dashboard title "{title}" should be visible'))
def verify_dashboard_title(dashboard_page, title):
    dashboard_page.verify_title(title)


@then(parsers.parse('the username "{username}" should be displayed on the dashboard'))
def verify_dashboard_username(dashboard_page, username):
    dashboard_page.verify_username(username)
