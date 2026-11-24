"""Logger utility: writes to console and logs/automation.log."""
import logging
import sys

from utils.config import Config

_FMT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"


def get_logger(name: str = "automation") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:          # avoid duplicate handlers
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False
    Config.LOG_DIR.mkdir(parents=True, exist_ok=True)

    file_handler = logging.FileHandler(Config.LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(_FMT))
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(logging.Formatter(_FMT))

    logger.addHandler(file_handler)
    logger.addHandler(console)
    return logger
