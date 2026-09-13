import logging
import sys
from pathlib import Path

# automation-tool-39 logging configuration
LOG_FILE = "automation.log"

def setup_logger(name: str = "automation-tool") -> logging.Logger:
    """Configures a standard logger for the automation tool."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # ensure handler uniqueness
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # console output
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # file output
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def log_event(logger: logging.Logger, message: str, level: str = "info"):
    """Wrapper to route messages based on severity string."""
    levels = {
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error,
        "debug": logger.debug
    }
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)