import math
from typing import Dict, List, Tuple, Union


def calculate_exp_to_next_level(
    current_level: int, current_exp: int, base_exp: int = 100
) -> Dict[str, int]:
    """Calculate remaining experience points and progress percentage for a character.

    Args:
        current_level: The character's current level.
        current_exp: The current amount of accumulated experience points.
        base_exp: Base multiplier used in the level scaling formula.

    Returns:
        A dictionary containing target EXP, remaining EXP, and percentage progress.
    """
    target_exp = int(base_exp * math.pow(current_level, 1.5))
    remaining_exp = max(0, target_exp - current_exp)
    progress_percent = min(100, int((current_exp / target_exp) * 100)) if target_exp > 0 else 100

    return {
        "target_exp": target_exp,
        "remaining_exp": remaining_exp,
        "progress_percent": progress_percent,
    }


def scale_coordinates(
    coords: Tuple[int, int],
    base_resolution: Tuple[int, int],
    target_resolution: Tuple[int, int],
) -> Tuple[int, int]:
    """Scale screen coordinates from a reference resolution to the target window size.

    Args:
        coords: Tuple of (x, y) pixel coordinates on the base resolution.
        base_resolution: Tuple of (width, height) of the original coordinate space.
        target_resolution: Tuple of (width, height) of the active game window.

    Returns:
        Scaled (x, y) coordinates adjusted for target resolution.
    """
    scale_x = target_resolution[0] / base_resolution[0]
    scale_y = target_resolution[1] / base_resolution[1]

    scaled_x = int(coords[0] * scale_x)
    scaled_y = int(coords[1] * scale_y)

    return (scaled_x, scaled_y)


def format_macro_sequence(
    keys: List[str], delay_ms: int = 50
) -> List[Dict[str, Union[str, int]]]:
    """Convert a sequence of key strings into a structured macro payload with delays.

    Args:
        keys: List of key names to press in sequence.
        delay_ms: Inter-key delay in milliseconds.

    Returns:
        List of event dictionaries ready for execution engine dispatch.
    """
    macro_events: List[Dict[str, Union[str, int]]] = []
    for key in keys:
        macro_events.append({"action": "key_down", "key": key, "delay_ms": 0})
        macro_events.append({"action": "key_up", "key": key, "delay_ms": delay_ms})

    return macro_events
