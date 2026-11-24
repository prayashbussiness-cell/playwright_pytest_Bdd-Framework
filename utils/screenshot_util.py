"""Screenshot utility: saves a PNG to /screenshots and attaches it to Allure."""
import re
from datetime import datetime

import allure

from utils.config import Config
from utils.logger import get_logger

log = get_logger(__name__)


def take_screenshot(page, name: str) -> str:
    Config.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", name)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = Config.SCREENSHOT_DIR / f"{safe}_{stamp}.png"
    page.screenshot(path=str(path), full_page=True)
    allure.attach.file(str(path), name=safe, attachment_type=allure.attachment_type.PNG)
    log.info("Screenshot saved: %s", path)
    return str(path)
