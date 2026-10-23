import time
import functools
import logging

logger = logging.getLogger(__name__)

def with_retry(max_attempts=3, delay=2):
    """Decorator to retry network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying...")
                    if attempt < max_attempts:
                        time.sleep(delay)
            logger.error(f"Operation failed after {max_attempts} attempts")
            raise last_exception
        return wrapper
    return decorator

@with_retry(max_attempts=3, delay=1)
def fetch_game_data(endpoint):
    """Simulate network call for gaming assets."""
    # Implementation logic for API requests would go here
    return {"status": "success", "data": "game_config_payload"}