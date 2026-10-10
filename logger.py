import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'automation-tool-39') -> logging.Logger:
    """Configures a rotating file logger for gaming automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Ensure logs directory exists
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Setup rotation: 5MB per file, keep 3 backups
    handler = RotatingFileHandler(
        'logs/automation.log', 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger