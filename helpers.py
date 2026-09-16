import random
import time
from typing import Tuple


def human_delay(min_seconds: float = 0.5, max_seconds: float = 1.5) -> None:
    """Simulates human-like reaction time using a randomized delay."""
    delay = random.uniform(min_seconds, max_seconds)
    jitter = random.gauss(0, (max_seconds - min_seconds) / 6)
    final_delay = max(min_seconds, min(max_seconds, delay + jitter))
    time.sleep(final_delay)


def scale_coordinates(
    x: int, y: int, base_res: Tuple[int, int], current_res: Tuple[int, int]
) -> Tuple[int, int]:
    """Scales relative UI coordinates based on target resolution."""
    scale_x = current_res[0] / base_res[0]
    scale_y = current_res[1] / base_res[1]
    return int(x * scale_x), int(y * scale_y)


def get_inventory_slot_center(
    slot_index: int,
    columns: int,
    start_x: int,
    start_y: int,
    slot_size: int = 40,
    spacing: int = 5,
) -> Tuple[int, int]:
    """Calculates the center pixel coordinates for a specific inventory grid slot."""
    row = slot_index // columns
    col = slot_index % columns

    x = start_x + col * (slot_size + spacing) + (slot_size // 2)
    y = start_y + row * (slot_size + spacing) + (slot_size // 2)
    return x, y


def is_within_bounds(
    x: int, y: int, screen_width: int, screen_height: int
) -> bool:
    """Checks if target click coordinates fall within screen boundaries."""
    return 0 <= x < screen_width and 0 <= y < screen_height
