import functools
import time
from typing import Callable, Any

# Cache for compute-intensive coordinate calculations
_coordinate_cache = {}

def memoize_coords(func: Callable) -> Callable:
    """Decorator for caching repetitive spatial calculations."""
    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in _coordinate_cache:
            _coordinate_cache[args] = func(*args)
        return _coordinate_cache[args]
    return wrapper

class DataProcessor:
    def __init__(self, buffer_size: int = 1024):
        self.buffer_size = buffer_size
        self.processed_count = 0

    @memoize_coords
    def calculate_offset(self, x: int, y: int, depth: int) -> tuple:
        """Complex math for gaming viewport rendering."""
        time.sleep(0.001)  # Simulate heavy CPU load
        return (x * depth, y * depth)

    def batch_process(self, data_points: list) -> list:
        """Optimized batch processing using list comprehension."""
        results = [
            self.calculate_offset(p[0], p[1], p[2]) 
            for p in data_points
        ]
        self.processed_count += len(results)
        return results

    def clear_cache(self) -> None:
        """Manual cache invalidation for memory management."""
        _coordinate_cache.clear()