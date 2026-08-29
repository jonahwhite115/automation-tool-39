import logging
from logging.handlers import RotatingFileHandler
import os

LOG_FILE = 'automation_tool.log'
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3
LOG_LEVEL = logging.INFO

def setup_logging():
    """Set up logger with rotation for the gaming automation tool."""
    logger = logging.getLogger('automation-tool-39')
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.setLevel(LOG_LEVEL)

    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, LOG_FILE)

    file_handler = RotatingFileHandler(
        log_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT
    )
    file_handler.setLevel(LOG_LEVEL)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info('Logger setup complete with rotation enabled')
    return logger

if __name__ == '__main__':
    logger = setup_logging()
    logger.info('Testing the logger')
    logger.warning('This is a test warning')