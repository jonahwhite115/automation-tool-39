import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_retries=3, delay=2):
    """Decorator for retrying network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    if attempt < max_retries:
                        time.sleep(delay)
            
            logger.error(f"Operation failed after {max_retries} attempts.")
            raise last_exception
        return wrapper
    return decorator