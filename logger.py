import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "automation_tool"):
    """Initializes a rotating file logger for gaming automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Ensure logs directory exists
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Setup file rotation: 5MB per file, keep 3 backups
    log_file = os.path.join(log_dir, f"{name}.log")
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5*1024*1024, 
        backupCount=3
    )
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    
    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        logger.addHandler(handler)
        
    # Optional console output for development
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger