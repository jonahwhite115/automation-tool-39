import functools
import time
import logging
from typing import Callable, Any

logger = logging.getLogger('automation-tool-39')

def memoize_with_ttl(ttl_seconds: int = 300) -> Callable:
    """Cache function results with time-to-live for game state data."""
    def decorator(func: Callable) -> Callable:
        cache = {}
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, frozenset(kwargs.items()))
            current_time = time.time()
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < ttl_seconds:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        return wrapper
    return decorator

def batch_process(data: list, batch_size: int = 100):
    """Generator for efficient chunking of large game entities."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

def profile_execution(func: Callable) -> Callable:
    """Decorator to log execution time for performance tuning."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logger.debug(f"Execution of {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper