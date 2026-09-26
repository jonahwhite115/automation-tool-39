import time
import functools
import logging

logger = logging.getLogger(__name__)

def with_retry(max_attempts=3, delay=2):
    """Decorator to retry network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    logger.warning(f"Attempt {attempts} failed: {e}")
                    if attempts >= max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@with_retry(max_attempts=3, delay=1)
def fetch_game_data(endpoint):
    """Simulated network request to a gaming API."""
    # Example implementation logic
    logger.info(f"Fetching data from {endpoint}")
    return {"status": "success", "data": "game_config_payload"}