import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'automation.log', level: int = logging.INFO):
    """Initializes a rotating file logger for automation-tool-39."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        # Ensure log directory exists
        os.makedirs('logs', exist_ok=True)
        log_path = os.path.join('logs', log_file)

        # 5MB per file, keep 5 backups
        handler = RotatingFileHandler(
            log_path, maxBytes=5*1024*1024, backupCount=5
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Stream logs to console as well
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Example usage for gaming modules
logger = setup_logger('automation-tool-39')