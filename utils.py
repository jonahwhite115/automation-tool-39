import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("automation_tool.utils")

def retry_on_failure(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """
    Decorator to retry a function call with exponential backoff and jitter.
    
    Useful for resilient network operations in gaming automation.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(f"Failed {func.__name__} after {retries} attempts: {e}")
                        raise
                    
                    # Apply exponential backoff with a random jitter
                    jitter = random.uniform(0.5, 1.5)
                    sleep_time = current_delay * jitter
                    logger.warning(
                        f"Retrying {func.__name__} in {sleep_time:.2f}s "
                        f"(Attempt {attempt}/{retries}) due to error: {e}"
                    )
                    time.sleep(sleep_time)
                    current_delay *= backoff
        return wrapper
    return decorator