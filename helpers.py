import random
import time
from typing import Tuple


def human_delay(min_seconds: float = 0.2, max_seconds: float = 1.5) -> None:
    """Delays execution by a random amount of time to mimic human behavior."""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)


def jitter_coordinate(
    x: int, y: int, max_offset: int = 5
) -> Tuple[int, int]:
    """Adds a small random offset to coordinates to simulate imperfect human clicks."""
    dx = random.randint(-max_offset, max_offset)
    dy = random.randint(-max_offset, max_offset)
    return x + dx, y + dy


def clamp_coordinates(
    x: int, y: int, screen_width: int, screen_height: int
) -> Tuple[int, int]:
    """Ensures targeted coordinates fall within the boundaries of the game screen."""
    clamped_x = max(0, min(x, screen_width - 1))
    clamped_y = max(0, min(y, screen_height - 1))
    return clamped_x, clamped_y


def calculate_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    """Calculates the Euclidean distance between two screen coordinates."""
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
