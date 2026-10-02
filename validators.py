import re
from typing import Tuple, Union, Set


def validate_screen_coordinates(x: int, y: int, screen_bounds: Tuple[int, int, int, int]) -> bool:
    """Validate if (x, y) coordinates fall within defined screen bounds (min_x, min_y, max_x, max_y)."""
    min_x, min_y, max_x, max_y = screen_bounds
    return min_x <= x <= max_x and min_y <= y <= max_y


def validate_hex_color(color_code: str) -> bool:
    """Check if a given string is a valid 6-digit hex color code used for pixel matching."""
    if not isinstance(color_code, str):
        return False
    pattern = r"^#?([0-9A-Fa-f]{6})$"
    return bool(re.match(pattern, color_code))


def validate_resource_percentage(value: Union[int, float]) -> float:
    """Validate and normalize resource percentage (health, mana, stamina) between 0.0 and 100.0."""
    if not isinstance(value, (int, float)):
        raise TypeError("Resource percentage must be a numerical value.")
    if value < 0.0 or value > 100.0:
        raise ValueError(f"Percentage {value} is out of bounds (0.0 - 100.0).")
    return float(value)


def validate_game_action(action: str, allowed_actions: Set[str]) -> bool:
    """Ensure the queued gaming automation action is recognized in the allowed action set."""
    if not isinstance(action, str):
        return False
    normalized_action = action.strip().lower()
    return normalized_action in {a.lower() for a in allowed_actions}
