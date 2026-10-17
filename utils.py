import time
import functools
import logging

# Configure logger for automation-tool-39
logger = logging.getLogger('automation-tool-39')

def retry_network_op(retries=3, delay=2.0, backoff=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries:
                        logger.error(f'Final attempt {attempt} failed for {func.__name__}: {e}')
                        raise
                    
                    logger.warning(f'Attempt {attempt} failed for {func.__name__}. Retrying in {current_delay}s...')
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

# Example usage for gaming API calls
@retry_network_op(retries=3, delay=1)
def fetch_game_data(url):
    # Simulate network operation
    logger.info(f'Fetching data from {url}')
    return {'status': 'success', 'data': 'mock_payload'}