import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=2, backoff=2):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

# Example usage for gaming API calls
@retry_network_op(retries=3, delay=1)
def fetch_server_status(endpoint):
    """Placeholder for actual requests library call."""
    # Simulate network instability
    import random
    if random.random() < 0.7:
        raise ConnectionError("Server unreachable")
    return {"status": "online", "ping": "24ms"}