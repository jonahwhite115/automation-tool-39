import time
import functools
import logging

# Setup logger for gaming automation tool
logger = logging.getLogger('automation-tool-39')

def retry_operation(max_retries=3, delay=2):
    """Decorator to implement exponential backoff retry logic."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_retries:
                        logger.error(f"Failed after {max_retries} attempts: {e}")
                        raise
                    sleep_time = delay * (2 ** (attempts - 1))
                    logger.warning(f"Retry {attempts}/{max_retries} after {sleep_time}s error: {e}")
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@retry_operation(max_retries=3, delay=1)
def fetch_game_data(endpoint):
    """Simulated network request to gaming server."""
    # Logic for interaction with game API
    return {'status': 'success', 'data': 'mock_payload'}