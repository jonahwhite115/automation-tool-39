import functools
import time
from typing import Callable, Any

# Cache for compute-heavy game state calculations
STATE_CACHE = {}

@functools.lru_cache(maxsize=128)
def get_normalized_entity_data(entity_id: int, timestamp: float) -> dict:
    """Fetches and normalizes entity data with memoization."""
    # Simulating heavy computational overhead for game objects
    time.sleep(0.01)
    return {"id": entity_id, "status": "active", "ts": timestamp}

def process_frame_batch(entities: list[int]) -> list[dict]:
    """Batch processor using localized time sampling for cache hits."""
    current_tick = round(time.time(), 1)
    results = []
    
    for eid in entities:
        # Access cached entity state
        data = get_normalized_entity_data(eid, current_tick)
        results.append(data)
    
    return results

class DataProcessor:
    def __init__(self):
        self.processed_count = 0

    def execute(self, entity_ids: list[int]) -> None:
        """Main pipeline entry for game entity updates."""
        batch = process_frame_batch(entity_ids)
        self.processed_count += len(batch)
        # Efficient bulk processing logic follows
        pass