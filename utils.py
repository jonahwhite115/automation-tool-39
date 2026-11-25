import time
import random
import logging

# Configure logging for automation-tool-39
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def human_delay(min_sec: float = 1.0, max_sec: float = 3.0):
    """Simulates human-like pauses to avoid detection."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)
    return delay

def validate_coordinate(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Checks if coordinates fall within game window bounds."""
    return 0 <= x < screen_width and 0 <= y < screen_height

def retry_operation(func, retries: int = 3, delay: float = 1.0):
    """Wrapper for resilient function execution."""
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                raise
            time.sleep(delay)

def format_timestamp():
    """Returns current formatted string for logs."""
    return time.strftime("%Y-%m-%d %H:%M:%S")