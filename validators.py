"""Input validation utilities for the game automation processing loop."""

from typing import Any, Dict, Tuple


class ValidationError(Exception):
    """Raised when game loop input data fails validation checks."""
    pass


def validate_coordinates(coords: Any, screen_bounds: Tuple[int, int] = (1920, 1080)) -> Tuple[int, int]:
    """Validate screen target coordinates are within valid bounds."""
    if not isinstance(coords, (tuple, list)) or len(coords) != 2:
        raise ValidationError(f"Invalid coordinate format: {coords}. Expected (x, y) tuple.")

    x, y = coords
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValidationError(f"Coordinates must be numeric values: ({x}, {y}).")

    max_x, max_y = screen_bounds
    if not (0 <= x <= max_x and 0 <= y <= max_y):
        raise ValidationError(f"Target coordinates ({x}, {y}) out of screen bounds {screen_bounds}.")

    return int(x), int(y)


def validate_action_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a raw game loop action payload before execution."""
    if not isinstance(payload, dict):
        raise ValidationError("Action payload must be a dictionary.")

    action_type = payload.get("action_type")
    allowed_actions = {"click", "key_press", "drag", "wait", "combo"}
    if action_type not in allowed_actions:
        raise ValidationError(f"Unsupported action type '{action_type}'. Allowed: {allowed_actions}")

    delay = payload.get("delay", 0.0)
    if not isinstance(delay, (int, float)) or delay < 0:
        raise ValidationError(f"Invalid execution delay: {delay}. Must be non-negative number.")

    if action_type in ("click", "drag"):
        if "target" not in payload:
            raise ValidationError(f"Action '{action_type}' requires a target coordinate.")
        validate_coordinates(payload["target"])

    return payload