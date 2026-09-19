import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger("automation.utils")

def retry_network_op(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry network operations with exponential backoff.
    Useful for game API requests, session heartbeats, and status checks.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            f"Network operation '{func.__name__}' failed after {max_retries} attempts: {err}"
                        )
                        raise
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for '{func.__name__}' failed ({err}). "
                        f"Retrying in {current_delay:.1f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
        return wrapper
    return decorator

def safe_execute_network_call(
    func: Callable,
    *args: Any,
    default_return: Any = None,
    **kwargs: Any
) -> Any:
    """Executes a network operation safely, returning a default value on failure."""
    try:
        return func(*args, **kwargs)
    except Exception as exc:
        logger.error(f"Execution failed for gaming service call: {exc}")
        return default_return
