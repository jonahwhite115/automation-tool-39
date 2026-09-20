import time
import random
from typing import Callable, Any, Optional

def retry_operation(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Attempts to execute a function with exponential backoff."""
    for i in range(retries):
        try:
            return func()
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(delay * (2 ** i))

def randomize_delay(base: float, jitter: float = 0.5) -> None:
    """Adds a small random wait to avoid detection."""
    sleep_time = base + random.uniform(0, jitter)
    time.sleep(sleep_time)

def format_coords(x: int, y: int) -> dict:
    """Converts raw pixel coordinates to standard dictionary format."""
    return {"x": int(x), "y": int(y)}

def is_within_bounds(x: int, y: int, width: int, height: int) -> bool:
    """Validates coordinates against screen dimensions."""
    return 0 <= x < width and 0 <= y < height