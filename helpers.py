import time
import random
import pyautogui

def sleep_random(min_sec=1.0, max_sec=3.0):
    """Wait for a random duration to mimic human behavior."""
    time.sleep(random.uniform(min_sec, max_sec))

def click_element(x, y, confidence=0.8):
    """Perform a mouse click at specific coordinates."""
    pyautogui.click(x, y)
    sleep_random(0.5, 1.2)

def screen_capture(region=None):
    """Capture a portion of the screen for image analysis."""
    return pyautogui.screenshot(region=region)

def get_screen_resolution():
    """Retrieve the current display dimensions."""
    return pyautogui.size()

def emergency_stop():
    """Force fail-safe trigger for automation."""
    pyautogui.FAILSAFE = True
    print("Automation safety protocols enabled.")

def type_command(text, interval=0.1):
    """Simulate keyboard typing for in-game commands."""
    pyautogui.typewrite(text, interval=interval)
    pyautogui.press('enter')

def is_pixel_color(x, y, target_color, tolerance=5):
    """Check if a pixel matches a specific RGB color."""
    pixel = pyautogui.pixel(x, y)
    return all(abs(p - t) <= tolerance for p, t in zip(pixel, target_color))