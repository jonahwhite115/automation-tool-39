import random
import time
from typing import Tuple


def random_delay(min_seconds: float = 0.1, max_seconds: float = 0.35) -> None:
    """Sleep for a randomized duration to simulate human reaction time."""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)


def calculate_health_percentage(current_hp: float, max_hp: float) -> float:
    """Calculate the remaining health percentage bounded between 0.0 and 100.0."""
    if max_hp <= 0:
        return 0.0
    percentage = (current_hp / max_hp) * 100.0
    return max(0.0, min(100.0, round(percentage, 2)))


def scale_coordinates(
    point: Tuple[int, int],
    base_resolution: Tuple[int, int],
    target_resolution: Tuple[int, int]
) -> Tuple[int, int]:
    """Scale screen coordinates from a base design resolution to a target resolution."""
    base_w, base_h = base_resolution
    target_w, target_h = target_resolution

    if base_w <= 0 or base_h <= 0:
        raise ValueError("Base resolution dimensions must be positive integers.")

    scale_x = target_w / base_w
    scale_y = target_h / base_h

    scaled_x = int(round(point[0] * scale_x))
    scaled_y = int(round(point[1] * scale_y))

    return (scaled_x, scaled_y)


def is_cooldown_ready(last_used_timestamp: float, cooldown_seconds: float) -> bool:
    """Check if an ability or action cooldown period has elapsed."""
    current_time = time.time()
    return (current_time - last_used_timestamp) >= cooldown_seconds
