"""Pytest setup/teardown: browser, context, page, screenshots on failure, logs, Allure."""
import os

import allure
import pytest
from playwright.sync_api import sync_playwright

from utils.config import Config
from utils.logger import get_logger
from utils.screenshot_util import take_screenshot

log = get_logger("conftest")


def pytest_addoption(parser):
    parser.addoption("--browser-name", default=Config.BROWSER,
                     choices=["chromium", "firefox", "webkit"],
                     help="Browser to run tests on")
    parser.addoption("--headed", action="store_true", default=False,
                     help="Run browser in headed mode")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store each phase's result on the test item so fixtures can detect failures."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="session")
def browser(request):
    name = request.config.getoption("--browser-name")
    headless = Config.HEADLESS and not request.config.getoption("--headed")
    log.info("Launching %s (headless=%s)", name, headless)
    with sync_playwright() as pw:
        br = getattr(pw, name).launch(headless=headless, slow_mo=Config.SLOW_MO)
        yield br
        log.info("Closing browser")
        br.close()


@pytest.fixture
def page(browser, request):
    context = browser.new_context(viewport={"width": 1366, "height": 768})
    pg = context.new_page()
    pg.set_default_timeout(Config.TIMEOUT)
    log.info("=== START: %s ===", request.node.name)

    yield pg

    rep = getattr(request.node, "rep_call", None)
    if rep is not None and rep.failed:
        log.error("Test FAILED: %s", request.node.name)
        take_screenshot(pg, f"FAILED_{request.node.name}")
    log.info("=== END: %s ===", request.node.name)
    context.close()


@pytest.fixture(autouse=True)
def attach_log_to_allure():
    """Attach only this test's log lines to the Allure report."""
    log_file = Config.LOG_FILE
    start = log_file.stat().st_size if log_file.exists() else 0
    yield
    if log_file.exists():
        with open(log_file, "r", encoding="utf-8") as f:
            f.seek(start)
            content = f.read()
        if content:
            allure.attach(content, name="test_log",
                          attachment_type=allure.attachment_type.TEXT)
