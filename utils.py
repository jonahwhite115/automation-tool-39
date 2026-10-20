import random
import time
from typing import Tuple


def get_grid_coordinates(
    index: int,
    columns: int,
    slot_size: Tuple[int, int],
    padding: Tuple[int, int],
    origin: Tuple[int, int]
) -> Tuple[int, int]:
    """Calculate absolute screen coordinates for a specific inventory grid slot."""
    row = index // columns
    col = index % columns
    
    x = origin[0] + col * (slot_size[0] + padding[0]) + slot_size[0] // 2
    y = origin[1] + row * (slot_size[1] + padding[1]) + slot_size[1] // 2
    return (x, y)


def is_color_within_tolerance(
    color1: Tuple[int, int, int],
    color2: Tuple[int, int, int],
    tolerance: int = 10
) -> bool:
    """Check if two RGB color tuples match within a given variance threshold."""
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))


def sleep_humanized(base_seconds: float, variance: float = 0.2) -> None:
    """Sleep for a randomized duration to simulate human reaction delay."""
    delta = random.uniform(-variance, variance)
    duration = max(0.01, base_seconds + delta)
    time.sleep(duration)


def clamp_to_screen(
    x: int,
    y: int,
    screen_bounds: Tuple[int, int]
) -> Tuple[int, int]:
    """Ensure x and y coordinates stay strictly within screen boundaries."""
    clamped_x = max(0, min(x, screen_bounds[0] - 1))
    clamped_y = max(0, min(y, screen_bounds[1] - 1))
    return (clamped_x, clamped_y)
