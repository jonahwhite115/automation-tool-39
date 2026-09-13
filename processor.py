import functools
import time
from typing import Dict, Any

# Cache for repetitive game state calculations
STATE_CACHE_SIZE = 1024

class GameProcessor:
    def __init__(self):
        self._metrics: Dict[str, float] = {}

    @functools.lru_cache(maxsize=STATE_CACHE_SIZE)
    def calculate_entity_path(self, start: tuple, target: tuple) -> list:
        """Compute path using cached results for performance"""
        # Simulated heavy pathfinding logic
        time.sleep(0.01)
        return [start, target]

    def process_batch(self, data_points: list) -> list:
        """Efficient batch processing of game events"""
        results = []
        start_time = time.perf_counter()
        
        # Use list comprehension for faster iteration
        results = [self._transform(d) for d in data_points]
        
        self._metrics['last_batch_duration'] = time.perf_counter() - start_time
        return results

    def _transform(self, item: Any) -> Any:
        """Internal transformation for batch pipeline"""
        return item.get('value', 0) * 1.05

    def clear_cache(self):
        """Reset memory for long-running processes"""
        self.calculate_entity_path.cache_clear()