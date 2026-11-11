import time
import random
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def random_sleep(min_sec: float = 1.0, max_sec: float = 3.0) -> None:
    """Inject random delay to mimic human behavior."""
    time.sleep(random.uniform(min_sec, max_sec))

def retry_operation(func: Callable, retries: int = 3, delay: float = 2.0) -> Any:
    """Execute function with simple retry logic for network stability."""
    last_ex = None
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            last_ex = e
            logger.warning(f"Attempt {i+1} failed: {e}")
            time.sleep(delay * (i + 1))
    raise last_ex

def format_currency(value: float) -> str:
    """Format gaming currency values for console output."""
    if value >= 1_000_000:
        return f"{value/1_000_000:.2f}M"
    if value >= 1_000:
        return f"{value/1_000:.1f}K"
    return str(int(value))

def validate_screen_bounds(x: int, y: int, width: int, height: int) -> bool:
    """Check if coordinates are within defined game window."""
    return 0 <= x <= width and 0 <= y <= height