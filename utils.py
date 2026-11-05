import functools
import time
from typing import Callable, Any, Dict

# Cache for repetitive gaming engine calculations
_cache: Dict[tuple, Any] = {}

def memoize_performance(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

def batch_process(data_list: list, chunk_size: int = 100):
    """Generator for memory-efficient iteration of game entity lists."""
    for i in range(0, len(data_list), chunk_size):
        yield data_list[i:i + chunk_size]

def benchmark_execution(func: Callable) -> Callable:
    """Log execution time for performance tuning cycles."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        if duration > 0.05:  # Log latency issues exceeding 50ms
            print(f"[PERF] {func.__name__} took {duration:.4f}s")
        return result
    return wrapper