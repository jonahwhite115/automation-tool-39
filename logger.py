import logging
from logging.handlers import RotatingFileHandler
import os

# Log file configuration for automation-tool-39
LOG_DIR = "logs"
LOG_FILE = "automation.log"
MAX_BYTES = 5 * 1024 * 1024  # 5MB
BACKUP_COUNT = 3

def setup_logger(name: str = "automation_tool") -> logging.Logger:
    """Configures a rotating file logger for the tool."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Setup rotating file handler
    file_path = os.path.join(LOG_DIR, LOG_FILE)
    handler = RotatingFileHandler(
        file_path, 
        maxBytes=MAX_BYTES, 
        backupCount=BACKUP_COUNT
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Also log to console for development visibility
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger