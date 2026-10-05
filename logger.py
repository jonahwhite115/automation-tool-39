import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "automation_tool"):
    """Configures a rotating file logger for gaming automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not os.path.exists("logs"):
        os.makedirs("logs")

    # 5MB per file, keep 3 historical backups
    handler = RotatingFileHandler(
        "logs/automation.log", 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger