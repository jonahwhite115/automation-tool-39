import time
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-39')

def click_at_coordinates(x: int, y: int, delay: float = 0.5):
    """Simulates mouse click at given screen coordinates."""
    logger.info(f"clicking at ({x}, {y})")
    time.sleep(delay)

def random_jitter(base_value: int, range_val: int = 5) -> int:
    """Adds random noise to coordinate values for human-like movement."""
    return base_value + random.randint(-range_val, range_val)

def wait_for_cooldown(seconds: int):
    """Handles pauses between game actions."""
    logger.info(f"waiting for {seconds} seconds cooldown")
    time.sleep(seconds)

def retry_operation(func, retries: int = 3, *args, **kwargs):
    """Executes function with basic retry mechanism for game stability."""
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.warning(f"attempt {attempt + 1} failed: {e}")
            time.sleep(1)
    raise RuntimeError("operation failed after max retries")