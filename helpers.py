import time
import random
import pyautogui

def sleep_random(min_sec: float = 0.5, max_sec: float = 2.0):
    """Wait for a random duration to simulate human input."""
    time.sleep(random.uniform(min_sec, max_sec))

def click_element(x: int, y: int, duration: float = 0.1):
    """Move mouse to coordinates and perform a click."""
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()

def is_pixel_match(x: int, y: int, expected_color: tuple, tolerance: int = 10) -> bool:
    """Check if a pixel at specific coordinates matches expected RGB values."""
    current_color = pyautogui.pixel(x, y)
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(current_color, expected_color))

def capture_screenshot(region: tuple = None) -> str:
    """Take a screenshot and return the file path."""
    timestamp = int(time.time())
    filename = f"capture_{timestamp}.png"
    pyautogui.screenshot(filename, region=region)
    return filename