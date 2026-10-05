import time
import functools
import logging
import requests

# Configure logger for automation-tool-39
logger = logging.getLogger('automation-tool-39')

def retry_network_op(retries=3, backoff=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f'Operation failed after {retries} attempts: {e}')
                        raise
                    wait_time = backoff ** attempt
                    logger.warning(f'Attempt {attempt} failed, retrying in {wait_time}s...')
                    time.sleep(wait_time)
        return wrapper
    return decorator

@retry_network_op(retries=3)
def fetch_game_data(url):
    """Fetches live game data from remote API endpoint."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()