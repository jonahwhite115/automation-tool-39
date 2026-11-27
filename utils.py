import time
import functools
import logging

# Set up logger for automation-tool-39 network tasks
logger = logging.getLogger('automation-tool-39')

def retry_network_operation(max_attempts=3, delay=2):
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
                    logger.warning(f"Attempt {attempts} failed: {e}. Retrying...")
                    if attempts == max_attempts:
                        logger.error("Max network retries reached.")
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

# Example usage for gaming API calls
@retry_network_operation(max_attempts=3, delay=1)
def fetch_game_data(endpoint):
    """Placeholder for actual network logic."""
    # Simulating volatile network connectivity
    import random
    if random.random() < 0.7:
        raise ConnectionError("Server connectivity issue")
    return {"status": "success", "data": "game_stats"}