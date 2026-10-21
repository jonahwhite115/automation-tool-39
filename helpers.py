import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_on_failure(retries=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """
    Decorator to retry network-dependent functions upon failure.
    
    :param retries: Number of attempts to make.
    :param delay: Seconds to wait between attempts.
    :param exceptions: Tuple of exceptions that trigger a retry.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}: {e}")
                    if attempt < retries - 1:
                        time.sleep(delay)
            logger.error(f"All {retries} attempts failed for {func.__name__}")
            raise last_exception
        return wrapper
    return decorator