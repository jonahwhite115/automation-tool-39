import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("automation_tool.utils")

def retry_on_failure(
    retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry network operations or API requests on specified exceptions.
    Features exponential backoff and randomized jitter to prevent thundering herds.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(f"Failed '{func.__name__}' after {retries} attempts: {e}")
                        raise e
                    
                    # Calculate backoff with optional jitter
                    sleep_time = delay
                    if jitter:
                        sleep_time += random.uniform(0, delay * 0.5)
                    
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed for '{func.__name__}': {e}. "
                        f"Retrying in {sleep_time:.2f} seconds..."
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor
            return func(*args, **kwargs)
        return wrapper
    return decorator