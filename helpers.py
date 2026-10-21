import time
import random
import pyautogui

def random_sleep(min_sec=0.5, max_sec=1.5):
    """Wait for a random duration to simulate human-like behavior."""
    time.sleep(random.uniform(min_sec, max_sec))

def click_element(x, y, confidence=0.8):
    """Perform a mouse click at specific coordinates."""
    pyautogui.click(x=x, y=y)
    random_sleep()

def get_screen_center():
    """Calculate the center point of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def press_key(key, duration=0.1):
    """Press and hold a keyboard key for a brief duration."""
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def log_status(message):
    """Simple timestamped log output for automation events."""
    timestamp = time.strftime('%H:%M:%S')
    print(f'[{timestamp}] {message}')

def safe_screenshot(filename='debug.png'):
    """Capture current screen state for verification."""
    img = pyautogui.screenshot()
    img.save(filename)
    log_status(f'screenshot saved to {filename}')