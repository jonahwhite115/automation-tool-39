import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures a standardized logger for automation-tool-39 components.

    Args:
        name: The name of the module or component.
        level: The logging threshold level.

    Returns:
        A configured logging.Logger instance.
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
    formatter: logging.Formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )
    
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

def log_performance(logger: logging.Logger, action: str, duration: float) -> None:
    """
    Logs the execution duration for specific gaming tasks.

    Args:
        logger: The logger instance to use.
        action: Name of the automated task performed.
        duration: Time elapsed in seconds.
    """
    logger.info(f"action: {action} | duration: {duration:.4f}s")