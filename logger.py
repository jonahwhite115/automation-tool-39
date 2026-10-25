import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-39', log_file='game_automation.log'):
    """
    Configures a rotating file logger for the gaming automation tool.
    Keeps logs at 5MB per file with a backup count of 3.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotation setup: 5MB max size per file, keeping 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Also output to console for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Initialize global logger instance
logger = setup_logger()