import time
import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-39')

def retry_network_op(retries=3, delay=2, backoff=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logger.error(f"Failed after {retries} attempts: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=1)
def fetch_game_data(url):
    """Example network call for gaming data."""
    # Logic for actual request would be here
    logger.info(f"Fetching data from {url}")
    return True