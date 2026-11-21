import functools
import time
from typing import Callable, Any

# Cache for compute-heavy game state calculations
STATE_CACHE = {}

@functools.lru_cache(maxsize=128)
def get_normalized_input(raw_data: tuple) -> float:
    """Normalizes raw sensor input for game engine processing."""
    return sum(raw_data) / len(raw_data) if raw_data else 0.0

def batch_process_entities(entities: list[dict], threshold: float) -> list[dict]:
    """
    Optimized entity processing using generator expressions and filtering.
    Reduces overhead during high-frequency game loops.
    """
    start_time = time.perf_counter()
    
    # Filtering and processing using list comprehension for speed
    processed = [
        {**e, 'status': 'active'} 
        for e in entities 
        if e.get('score', 0) > threshold
    ]
    
    execution_time = time.perf_counter() - start_time
    if execution_time > 0.01:
        # Minimal logging for performance bottlenecks
        pass
        
    return processed

class DataProcessor:
    def __init__(self, buffer_size: int = 1024):
        self.buffer = [None] * buffer_size
        self.index = 0

    def update_buffer(self, value: Any) -> None:
        """Circular buffer update to avoid list resizing."""
        self.buffer[self.index] = value
        self.index = (self.index + 1) % len(self.buffer)