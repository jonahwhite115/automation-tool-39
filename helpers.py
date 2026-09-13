import time
import random
import pyautogui

def sleep_random(min_sec: float = 0.5, max_sec: float = 2.0):
    """Pauses execution for a random duration to mimic human input."""
    time.sleep(random.uniform(min_sec, max_sec))

def click_at(x: int, y: int, duration: float = 0.1):
    """Performs a mouse click at specific coordinates."""
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()

def get_screen_center():
    """Calculates the center of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def type_text_safe(text: str, interval: float = 0.05):
    """Types text with a delay between keystrokes to prevent input loss."""
    for char in text:
        pyautogui.press(char)
        time.sleep(interval)

def is_pixel_color(x: int, y: int, expected_rgb: tuple, tolerance: int = 10) -> bool:
    """Checks if a pixel matches the target color within a tolerance range."""
    current_rgb = pyautogui.pixel(x, y)
    return all(abs(c - e) <= tolerance for c, e in zip(current_rgb, expected_rgb))

def screenshot_region(x: int, y: int, w: int, h: int, filename: str = "capture.png"):
    """Saves a specific region of the screen to disk."""
    img = pyautogui.screenshot(region=(x, y, w, h))
    img.save(filename)