import random
import time
from typing import Tuple


def human_delay(min_seconds: float = 0.1, max_seconds: float = 0.5) -> None:
    """Simulate human reaction time with a randomized sleep duration."""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)


def calculate_health_percentage(current_hp: int, max_hp: int) -> float:
    """Calculate current health percentage safely."""
    if max_hp <= 0:
        return 0.0
    return round(max(0.0, min(100.0, (current_hp / max_hp) * 100)), 2)


def grid_to_screen_coords(
    row: int,
    col: int,
    start_x: int,
    start_y: int,
    slot_size: int,
    padding: int = 2,
) -> Tuple[int, int]:
    """Convert inventory grid row/col to screen center coordinates."""
    center_x = start_x + col * (slot_size + padding) + (slot_size // 2)
    center_y = start_y + row * (slot_size + padding) + (slot_size // 2)
    return center_x, center_y


def is_within_bounds(
    point: Tuple[int, int], region: Tuple[int, int, int, int]
) -> bool:
    """Check if (x, y) point lies within region (x, y, width, height)."""
    x, y = point
    rx, ry, rwidth, rheight = region
    return rx <= x <= rx + rwidth and ry <= y <= ry + rheight


def format_cooldown(seconds_remaining: float) -> str:
    """Format cooldown time into human readable format."""
    if seconds_remaining <= 0:
        return "Ready"
    if seconds_remaining < 60:
        return f"{seconds_remaining:.1f}s"
    minutes = int(seconds_remaining // 60)
    secs = int(seconds_remaining % 60)
    return f"{minutes:02d}:{secs:02d}"
