import functools
import time
import logging
from typing import Callable, Any

# Logger setup for automation-tool-39 core performance monitoring
logger = logging.getLogger('automation_tool_39.utils')

CACHE_TTL = 300
_cache = {}

def memoize_with_ttl(ttl: int = CACHE_TTL) -> Callable:
    """Performance optimization: cache heavy gaming state lookups."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = (func.__name__, args, frozenset(kwargs.items()))
            now = time.time()
            if key in _cache and now - _cache[key]['timestamp'] < ttl:
                return _cache[key]['value']
            
            result = func(*args, **kwargs)
            _cache[key] = {'value': result, 'timestamp': now}
            return result
        return wrapper
    return decorator

def batch_process(items: list, chunk_size: int = 100):
    """Generator for efficient batching of game entity updates."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def get_system_load_factor() -> float:
    """Calculate throttling factor to preserve CPU for game process."""
    # Placeholder for actual system monitor hook
    return 0.85