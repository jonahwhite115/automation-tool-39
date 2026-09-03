import time
import random
import pyautogui

def sleep_random(min_sec: float = 0.5, max_sec: float = 2.0):
    """Wait for a randomized duration to simulate human-like behavior."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def click_at(x: int, y: int, confidence: float = 0.9):
    """Perform a mouse click at specific coordinates with delay."""
    pyautogui.click(x, y)
    sleep_random()

def get_screen_center():
    """Calculate center of primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def verify_pixel_color(x: int, y: int, target_rgb: tuple, tolerance: int = 10):
    """Check if pixel color matches target within a threshold."""
    pixel = pyautogui.pixel(x, y)
    return all(abs(p - t) <= tolerance for p, t in zip(pixel, target_rgb))

def log_event(message: str):
    """Simple console output wrapper for automation status."""
    timestamp = time.strftime("%H:%M:%S")
    print(f"[{timestamp}] [automation-tool-39]: {message}")