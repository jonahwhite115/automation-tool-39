import time
import random
import logging

# Configure basic logger for automation operations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-39')

def sleep_randomly(min_sec: float = 1.0, max_sec: float = 3.0):
    """Introduce human-like delays between automation actions."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def retry_operation(func, retries: int = 3, delay: float = 2.0):
    """Decorator-like utility for robust network or UI interaction."""
    last_exception = None
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    raise last_exception

def format_timestamp(ts: float) -> str:
    """Convert epoch time to standard readable string format."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

def get_random_user_agent() -> str:
    """Return a randomized user agent string for stealth."""
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/91.0.4472",
        "Mozilla/5.0 (X11; Linux x86_64) Firefox/89.0"
    ]
    return random.choice(agents)