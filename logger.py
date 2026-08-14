import logging
from typing import Any, Optional


def setup_logger(name: str, level: Optional[int] = logging.INFO) -> logging.Logger:
    """Set up a logger with the specified name and logging level."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def log_info(logger: logging.Logger, message: str, *args: Any) -> None:
    """Log an informational message."""
    logger.info(message, *args)


def log_error(logger: logging.Logger, message: str, *args: Any) -> None:
    """Log an error message."""
    logger.error(message, *args)


def log_warning(logger: logging.Logger, message: str, *args: Any) -> None:
    """Log a warning message."""
    logger.warning(message, *args)


def log_debug(logger: logging.Logger, message: str, *args: Any) -> None:
    """Log a debug message."""
    logger.debug(message, *args)