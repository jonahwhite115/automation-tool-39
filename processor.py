import time
import random
from typing import Dict, Any

def calculate_cooldown(base_time: int, jitter_range: int = 5) -> float:
    """Calculates randomized cooldown to simulate human input."""
    jitter = random.uniform(0, jitter_range)
    return float(base_time + jitter)

def format_game_state(data: Dict[str, Any]) -> str:
    """Converts raw API dict into log-friendly string."""
    parts = [f"{k.upper()}: {v}" for k, v in data.items()]
    return " | ".join(parts)

def validate_inventory_slots(items: list, max_capacity: int = 20) -> bool:
    """Checks if inventory capacity is within limits."""
    return len(items) <= max_capacity

def execute_with_retry(func, retries: int = 3, *args, **kwargs):
    """Wraps execution with basic retry logic."""
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt == retries - 1:
                raise e
            time.sleep(1)
    return None