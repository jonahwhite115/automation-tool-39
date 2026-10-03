import random
import time
from typing import Tuple


def get_randomized_delay(base_seconds: float, variance_percent: float = 0.2) -> float:
    """Calculate a randomized delay duration to simulate human reaction times."""
    min_delay = base_seconds * (1.0 - variance_percent)
    max_delay = base_seconds * (1.0 + variance_percent)
    return max(0.0, random.uniform(min_delay, max_delay))


def sleep_with_jitter(base_seconds: float, variance_percent: float = 0.2) -> None:
    """Pause execution for a randomized duration."""
    delay = get_randomized_delay(base_seconds, variance_percent)
    time.sleep(delay)


def scale_coordinates(
    x: int, y: int, source_res: Tuple[int, int], target_res: Tuple[int, int]
) -> Tuple[int, int]:
    """Scale click coordinates from a reference screen resolution to target resolution."""
    src_w, src_h = source_res
    tgt_w, tgt_h = target_res

    if src_w <= 0 or src_h <= 0:
        raise ValueError("Source resolution dimensions must be positive.")

    scaled_x = int(round((x / src_w) * tgt_w))
    scaled_y = int(round((y / src_h) * tgt_h))
    return scaled_x, scaled_y


def is_color_match(
    rgb1: Tuple[int, int, int], rgb2: Tuple[int, int, int], tolerance: int = 15
) -> bool:
    """Check if two RGB color tuples match within a given per-channel tolerance."""
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(rgb1, rgb2))
