import logging
import os
from typing import Optional

def setup_logger(name: str, log_file: str = 'automation.log') -> logging.Logger:
    """Configures a robust logger for gaming automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    try:
        # Ensure directory exists for the log file
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
            
        handler = logging.FileHandler(log_file, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    except (PermissionError, OSError) as e:
        # Fallback to console if file system access fails
        print(f"Critical: Could not initialize log file: {e}")
        console_handler = logging.StreamHandler()
        logger.addHandler(console_handler)
        
    return logger

def safe_log(logger: logging.Logger, message: str, level: str = 'info') -> None:
    """Thread-safe logging wrapper for game state monitoring."""
    levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error
    }
    
    try:
        log_func = levels.get(level.lower(), logger.info)
        log_func(str(message))
    except Exception as e:
        print(f"Logging failure: {e}")