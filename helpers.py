import time
import random
import pyautogui
import logging

# Configure basic logger for automation-tool-39
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-39')

def human_sleep(min_sec=1.0, max_sec=3.0):
    """Simulate human behavior with random delays."""
    sleep_time = random.uniform(min_sec, max_sec)
    time.sleep(sleep_time)

def safe_click(x, y, confidence=0.8):
    """Perform a click with randomized offset to avoid bot detection."""
    try:
        offset_x = x + random.randint(-2, 2)
        offset_y = y + random.randint(-2, 2)
        pyautogui.moveTo(offset_x, offset_y, duration=0.2)
        pyautogui.click()
        logger.info(f"Clicked at {offset_x}, {offset_y}")
    except Exception as e:
        logger.error(f"Click failure at {x}, {y}: {e}")

def get_screen_center():
    """Retrieve central coordinates of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def retry_operation(func, retries=3, delay=2):
    """Wrapper for retrying unstable gaming operations."""
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {i+1} failed: {e}. Retrying...")
            time.sleep(delay)
    return None