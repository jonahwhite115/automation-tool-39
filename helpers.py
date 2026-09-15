import time
import random
from typing import Any, Callable

def retry_operation(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Execute function with simple linear retry logic."""
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            if i == retries - 1:
                raise e
            time.sleep(delay * (2 ** i))

def format_timestamp(timestamp: float) -> str:
    """Convert epoch time to human readable string."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

def get_random_jitter(base_delay: float, factor: float = 0.2) -> float:
    """Add jitter to delays to avoid detection."""
    jitter = base_delay * factor
    return base_delay + random.uniform(-jitter, jitter)

def sanitize_input(value: str) -> str:
    """Remove whitespace and special characters from gaming inputs."""
    return "".join(char for char in value if char.isalnum())

def log_performance(func: Callable) -> Callable:
    """Decorator for tracking function execution time."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[PERF] {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper