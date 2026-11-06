import math
import random
import time
from typing import Tuple, Optional


def human_delay(min_seconds: float = 0.1, max_seconds: float = 0.3) -> None:
    """Sleep for a randomized duration to simulate human reaction speed."""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)


def calculate_screen_offset(
    base_pos: Tuple[int, int],
    grid_index: int,
    grid_cols: int,
    slot_dimensions: Tuple[int, int]
) -> Tuple[int, int]:
    """Calculate absolute pixel coordinates for an item slot in a game UI grid."""
    col = grid_index % grid_cols
    row = grid_index // grid_cols
    
    x = base_pos[0] + (col * slot_dimensions[0]) + (slot_dimensions[0] // 2)
    y = base_pos[1] + (row * slot_dimensions[1]) + (slot_dimensions[1] // 2)
    return (x, y)


def color_distance(color1: Tuple[int, int, int], color2: Tuple[int, int, int]) -> float:
    """Calculate Euclidean distance between two RGB colors for UI matching."""
    r_diff = color1[0] - color2[0]
    g_diff = color1[1] - color2[1]
    b_diff = color1[2] - color2[2]
    return math.sqrt(r_diff ** 2 + g_diff ** 2 + b_diff ** 2)


def is_color_match(
    pixel_color: Tuple[int, int, int],
    target_color: Tuple[int, int, int],
    tolerance: float = 15.0
) -> bool:
    """Check if a pixel color matches target RGB within tolerance threshold."""
    return color_distance(pixel_color, target_color) <= tolerance


def parse_cooldown_text(text: str) -> Optional[float]:
    """Parse remaining cooldown seconds from formatted text strings."""
    cleaned = text.strip().lower()
    if not cleaned:
        return None
    try:
        if cleaned.endswith("s"):
            return float(cleaned[:-1])
        if cleaned.endswith("m"):
            return float(cleaned[:-1]) * 60.0
        return float(cleaned)
    except ValueError:
        return None
