import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_file: str = 'automation.log', level: int = logging.INFO) -> logging.Logger:
    """
    Configures a rotating file logger for automation-tool-39.
    Keeps 5 files of 5MB each.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotation setup: max 5MB, keep 5 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=5
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Stream to console as well
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger