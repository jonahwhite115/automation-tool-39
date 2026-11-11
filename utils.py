import time
import functools
import logging

# Logger setup for automation-tool-39
logger = logging.getLogger('automation-tool-39')

def retry_network_op(retries=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """Decorator to retry network-dependent functions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            logger.error(f"Function {func.__name__} failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=5)
def fetch_game_data(endpoint):
    """Example network operation for game server communication."""
    # Simulating actual network call logic
    logger.info(f"Connecting to {endpoint}...")
    return {"status": "success", "data": []}