import os
import sys
import logging
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
DEFAULT_LOG_FILE = "bot_automation.log"
MAX_BYTES = 5 * 1024 * 1024  # 5 MB max per log file
BACKUP_COUNT = 5             # Maintain up to 5 historical logs


def setup_logger(name: str = "automation_tool", log_file: str = DEFAULT_LOG_FILE, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger with standard console and rotating file output.
    Designed for continuous gaming automation sessions.
    """
    os.makedirs(LOG_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, log_file)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid attaching handlers multiple times if logger is already set up
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console output stream for runtime tracking
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Size-based rotating file handler to restrict disk usage
    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=MAX_BYTES,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


# Pre-configured instance ready for module imports
bot_logger = setup_logger()
