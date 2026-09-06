import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-39', log_file='game_automation.log', level=logging.INFO):
    """Initializes a rotating file logger for the automation tool."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate logs at 5MB, keep 3 backups
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Optional stream handler for console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instantiate default project logger
logger = setup_logger()