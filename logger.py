import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "game_bot", log_file: str = "logs/automation.log") -> logging.Logger:
    """
    Configures a standard rotating file logger and console output.
    Designed for persistent tracking of gaming automation tasks.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        return logger

    # Shared formatter for standard, readable gaming bot output
    log_format = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console output for quick manual tracking
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Ensure logs directory exists before mounting rotating file handler
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Rotating handler setup (limits to 3 backup logs of 2MB each)
    try:
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=2 * 1024 * 1024,  # 2MB limits
            backupCount=3,
            encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    except (OSError, PermissionError) as error:
        logger.warning(f"Could not setup rotating file log, falling back to console only: {error}")

    return logger

game_logger = setup_logger()