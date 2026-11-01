import time
import functools
import logging
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)

def retry_network_op(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries network operations for game server APIs 
    and asset downloads using exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_attempts:
                        logger.error(
                            "[Network] Call to %s failed after %d attempts: %s",
                            func.__name__, max_attempts, err
                        )
                        raise
                    
                    logger.warning(
                        "[Network] %s failed (attempt %d/%d). Retrying in %.2fs... Error: %s",
                        func.__name__, attempt, max_attempts, current_delay, err
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
        return wrapper
    return decorator
