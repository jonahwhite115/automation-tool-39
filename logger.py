import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'automation-tool-39', log_file: str = 'app.log') -> logging.Logger:
    """Configures a rotating file logger for gaming automation."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if function is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # File rotation: 5MB per file, keep 3 backups
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    # Also log to console for debugging
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)
    
    return logger