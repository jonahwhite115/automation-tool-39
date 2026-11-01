import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-39', log_file='automation.log', level=logging.INFO):
    """Initializes a rotating file logger for gaming automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        # File rotation: 5MB per file, keep 3 backup files
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        
        # Standard formatting for audit and debugging
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        
        # Console output for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Instance for global use
logger = setup_logger()