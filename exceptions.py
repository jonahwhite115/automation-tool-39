import time
import functools
import logging

logger = logging.getLogger(__name__)

class NetworkError(Exception):
    """Custom exception for network-related failures."""
    pass

def retry_on_failure(max_attempts=3, delay=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError, NetworkError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt {attempts} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
        return wrapper
    return decorator