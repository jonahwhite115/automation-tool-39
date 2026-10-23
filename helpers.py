import math
import random
import time
from typing import Tuple


def human_delay(min_seconds: float = 0.1, max_seconds: float = 0.35) -> None:
    """Pause execution for a randomized duration to simulate human input."""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)


def get_random_point_in_rect(
    x: int, y: int, width: int, height: int, padding: int = 4
) -> Tuple[int, int]:
    """Calculate a random click target inside a UI bounding box with safe padding."""
    inner_x1 = x + padding
    inner_y1 = y + padding
    inner_x2 = max(inner_x1, x + width - padding)
    inner_y2 = max(inner_y1, y + height - padding)

    target_x = random.randint(inner_x1, inner_x2)
    target_y = random.randint(inner_y1, inner_y2)
    return target_x, target_y


def is_color_similar(
    rgb1: Tuple[int, int, int], rgb2: Tuple[int, int, int], tolerance: int = 15
) -> bool:
    """Check if two RGB pixel colors are visually similar within a tolerance threshold."""
    r_diff = abs(rgb1[0] - rgb2[0])
    g_diff = abs(rgb1[1] - rgb2[1])
    b_diff = abs(rgb1[2] - rgb2[2])
    return (r_diff + g_diff + b_diff) / 3 <= tolerance


def scale_coords(
    x: int, y: int, base_res: Tuple[int, int], current_res: Tuple[int, int]
) -> Tuple[int, int]:
    """Scale screen coordinates from a base screen resolution to current display target."""
    scale_x = current_res[0] / base_res[0]
    scale_y = current_res[1] / base_res[1]
    return round(x * scale_x), round(y * scale_y)
