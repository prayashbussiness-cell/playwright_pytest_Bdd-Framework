"""Central configuration. Override anything with environment variables."""
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent


class Config:
    # >>> CHANGE THIS to your real login page URL (or set env var BASE_URL) <<<
    BASE_URL = os.getenv("BASE_URL", "http://localhost:3000/login")

    BROWSER = os.getenv("BROWSER", "chromium")      # chromium | firefox | webkit
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))         # ms between actions
    TIMEOUT = int(os.getenv("TIMEOUT", "15000"))     # ms

    SCREENSHOT_DIR = ROOT_DIR / "screenshots"
    LOG_DIR = ROOT_DIR / "logs"
    LOG_FILE = LOG_DIR / "automation.log"
    ALLURE_RESULTS = ROOT_DIR / "reports" / "allure-results"
