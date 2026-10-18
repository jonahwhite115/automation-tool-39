import functools
import time
from typing import Callable, Any

# Cache for repetitive game state calculations
STATE_CACHE = {}

def memoize_state(func: Callable) -> Callable:
    """Cache processor results based on input state."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in STATE_CACHE:
            STATE_CACHE[key] = func(*args, **kwargs)
        return STATE_CACHE[key]
    return wrapper

class GameProcessor:
    def __init__(self, buffer_size: int = 1000):
        self.buffer_size = buffer_size
        self.processed_count = 0

    @memoize_state
    def calculate_frame_delta(self, state_id: int, intensity: float) -> float:
        """High-cost math for game entity updates."""
        # Simulate intensive computation
        result = (state_id * 3.14159) ** intensity
        return result

    def clear_cache(self) -> None:
        """Prevent memory leaks in long-running processes."""
        STATE_CACHE.clear()

    def process_batch(self, items: list) -> list:
        """Process item list with optimized batch execution."""
        results = []
        for item in items:
            results.append(self.calculate_frame_delta(item['id'], item['val']))
            self.processed_count += 1
        
        # Auto-clear cache if buffer threshold reached
        if self.processed_count > self.buffer_size:
            self.clear_cache()
            self.processed_count = 0
        return results