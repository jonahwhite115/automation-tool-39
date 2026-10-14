import time
import functools
import logging
from typing import Callable, Any

# Configure logger for automation-tool-39 network tasks
logger = logging.getLogger("automation-tool-39")

def retry_network_operation(max_retries: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            logger.error(f"Operation failed after {max_retries} attempts: {last_exception}")
            raise last_exception
        return wrapper
    return decorator

# Example usage:
# @retry_network_operation(max_retries=3, delay=2.0)
# def fetch_game_data(url: str):
#     # Network request logic here
#     pass