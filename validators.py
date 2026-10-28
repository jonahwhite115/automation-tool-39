import time
import functools
import logging

logger = logging.getLogger('automation-tool-39')

def retry_on_failure(max_attempts=3, delay=2.0, backoff=2):
    """Decorator to retry network-dependent operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt {attempts} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

def validate_network_response(data):
    """Basic validation check for incoming API payloads."""
    if not data:
        raise ValueError("Empty response received from server")
    if not isinstance(data, dict):
        raise TypeError("Invalid data format: expected dictionary")
    return True