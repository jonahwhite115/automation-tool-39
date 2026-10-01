import time
import random
import logging

# Configure basic logger for automation-tool-39
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-39')

def sleep_randomly(min_sec=1.0, max_sec=3.0):
    """Simulates human-like delays to avoid detection."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)
    return delay

def validate_game_state(state, expected_keys):
    """Checks if all required keys exist in the game state dict."""
    if not isinstance(state, dict):
        return False
    return all(key in state for key in expected_keys)

def format_coords(x, y):
    """Standardizes coordinate tuples for interaction events."""
    return (int(x), int(y))

def retry_operation(func, retries=3, delay=1):
    """Decorator-like execution wrapper for volatile game actions."""
    last_error = None
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            last_error = e
            logger.warning(f"Attempt {i+1} failed, retrying in {delay}s...")
            time.sleep(delay)
    logger.error(f"Operation failed after {retries} attempts: {last_error}")
    return None

def log_event(message, level="info"):
    """Standardized logging wrapper for automation tracking."""
    if level == "info":
        logger.info(f"[GAME_EVENT] {message}")
    elif level == "error":
        logger.error(f"[GAME_ERROR] {message}")