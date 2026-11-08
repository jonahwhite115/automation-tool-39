import functools
import time
from typing import Callable, Any

# Cache for frequently accessed game state properties
_state_cache = {}

def memoize_state(func: Callable) -> Callable:
    """Performance decorator to reduce repetitive game state calculations."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, tuple(kwargs.items()))
        if key not in _state_cache:
            _state_cache[key] = func(*args, **kwargs)
        return _state_cache[key]
    return wrapper

class EngineProcessor:
    """Handles high-frequency automation loops with optimized cycles."""
    def __init__(self, tick_rate: float = 0.1):
        self.tick_rate = tick_rate

    @memoize_state
    def get_world_coordinates(self, entity_id: int) -> tuple:
        # Simulate intensive coordinate lookup operation
        time.sleep(0.01)
        return (entity_id * 1.5, entity_id * 2.0)

    def run_cycle(self, entity_id: int):
        # Execute logic using cached data to reduce latency
        coords = self.get_world_coordinates(entity_id)
        return f"Processing entity at {coords}"

def clear_cache():
    """Manual memory management for automation sessions."""
    _state_cache.clear()