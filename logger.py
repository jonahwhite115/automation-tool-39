import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "automation-tool-39", log_file: str = "game_automation.log") -> logging.Logger:
    """Initializes a rotating file logger for gaming automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        # Rotate files at 5MB, keep 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        # Optional: log to console as well
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Instantiate standard application logger
logger = setup_logger()