import time
import random
import logging

# Core automation helper functions for game interaction

logger = logging.getLogger(__name__)

def random_sleep(min_sec=1.0, max_sec=3.0):
    """Simulate human-like delays between actions."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)
    return delay

def retry_operation(func, retries=3, backoff=2.0):
    """Execute a function with basic retry logic."""
    last_ex = None
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {i+1} failed: {e}")
            last_ex = e
            time.sleep(backoff * (i + 1))
    raise last_ex

def format_coords(x, y, offset=0):
    """Apply screen offsets to coordinate pairs."""
    return (x + offset, y + offset)

def validate_game_state(state, expected_keys):
    """Check if game state dict contains required keys."""
    if not isinstance(state, dict):
        return False
    return all(key in state for key in expected_keys)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info("core automation helpers initialized")