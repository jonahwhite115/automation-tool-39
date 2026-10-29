import time
import random
import logging

# Configure basic logger for automation operations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-39')

def sleep_randomly(min_sec: float = 1.0, max_sec: float = 3.0):
    """Simulates human-like delay between gaming actions."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def format_timestamp(ts: float) -> str:
    """Converts epoch time to a readable string for logs."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

def retry_operation(func, retries: int = 3, delay: float = 2.0):
    """Simple decorator logic for unstable game API calls."""
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                raise
            time.sleep(delay)

def get_screen_center(width: int, height: int) -> tuple:
    """Calculates coordinate center for UI interaction."""
    return (width // 2, height // 2)

def validate_game_process(process_name: str) -> bool:
    """Placeholder for system process existence check."""
    import psutil
    return any(p.name() == process_name for p in psutil.process_iter(['name']))