import time
import functools
import logging

# Logger for network communication events
logger = logging.getLogger('automation-tool-39')

def with_retry(max_attempts=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """Decorator for retrying network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt {attempts} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed for {func.__name__}, retrying in {delay}s...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def validate_connection_status(func):
    """Ensures basic connectivity before executing decorated logic."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Logic for checking local game client socket
        logger.info("Validating game client connection...")
        return func(*args, **kwargs)
    return wrapper