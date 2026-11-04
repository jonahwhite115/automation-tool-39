import time
import functools
import logging

# Logger setup for automation-tool-39
logger = logging.getLogger('automation-tool-39')

def retry_on_network_failure(max_retries=3, delay=2):
    """Decorator to retry network-dependent operations."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_retries:
                        logger.error(f"Failed after {max_retries} attempts: {e}")
                        raise
                    logger.warning(f"Attempt {attempts} failed, retrying in {delay}s...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

class NetworkError(Exception):
    """Custom exception for gaming network services."""
    pass

class RateLimitError(Exception):
    """Raised when API requests exceed threshold."""
    pass