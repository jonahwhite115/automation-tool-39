import time
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-39')

def sleep_random(min_sec: float = 1.0, max_sec: float = 3.0) -> None:
    """Pauses execution for a randomized duration to simulate human input."""
    duration = random.uniform(min_sec, max_sec)
    time.sleep(duration)

def format_coords(x: int, y: int) -> dict:
    """Converts raw coordinate pairs into standardized dictionaries."""
    return {'x': x, 'y': y}

def retry_operation(func, retries: int = 3, delay: float = 1.0):
    """Retries a provided function upon failure with delay."""
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {i+1} failed: {e}")
            time.sleep(delay)
    return None

def is_valid_range(value: int, min_val: int, max_val: int) -> bool:
    """Validates that a numeric input falls within game bounds."""
    return min_val <= value <= max_val

def log_event(message: str, level: str = "info") -> None:
    """Standardized logging for gaming automation events."""
    if level == "error":
        logger.error(message)
    else:
        logger.info(message)