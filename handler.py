import time
import random
import logging

# Configure logging for automation-tool-39
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-39')

def sleep_randomly(min_sec=1, max_sec=5):
    """Simulates human-like delays to avoid anti-cheat detection."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)
    return delay

def validate_game_state(state, expected_keys):
    """Ensures the game data structure is valid before processing."""
    if not isinstance(state, dict):
        return False
    return all(key in state for key in expected_keys)

def retry_operation(func, retries=3, *args, **kwargs):
    """Retries a function operation with exponential backoff."""
    for i in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.warning(f"Attempt {i+1} failed: {e}")
            if i == retries - 1:
                raise
            time.sleep(2 ** i)

def format_player_coords(x, y, z):
    """Normalizes coordinate output for logging purposes."""
    return f"[{x:.2f}, {y:.2f}, {z:.2f}]"

def get_session_stats(kills, deaths):
    """Calculates basic player performance ratio."""
    if deaths == 0:
        return float(kills)
    return kills / deaths