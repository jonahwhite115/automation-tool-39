import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts: int = 3, delay: float = 2.0):
    """Decorator to retry network calls on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (2 ** attempt))
            logger.error(f"Operation {func.__name__} failed after {max_attempts} attempts")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, delay=1.0)
def fetch_game_data(endpoint: str):
    """Simulated network fetch operation for automation tool."""
    # Example logic for interaction with game servers
    pass