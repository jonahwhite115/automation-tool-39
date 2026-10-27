import time
import random
from typing import Any, List, Optional

def format_game_data(raw_input: dict) -> dict:
    """Standardizes incoming telemetry from game client."""
    return {
        "player_id": raw_input.get("uid", 0),
        "timestamp": time.time(),
        "payload": raw_input.get("data", {}),
        "version": "1.0.4"
    }

def retry_operation(func: callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Generic execution wrapper for unstable game endpoints."""
    last_exception = None
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            time.sleep(delay * (2 ** attempt))
    raise last_exception

def filter_invalid_coords(coords: List[tuple]) -> List[tuple]:
    """Sanitizes coordinate tuples for pathfinding operations."""
    return [c for c in coords if isinstance(c, tuple) and len(c) == 2]

def generate_jitter(base_delay: float) -> float:
    """Adds random noise to timing for anti-detection."""
    return base_delay * (0.8 + random.random() * 0.4)