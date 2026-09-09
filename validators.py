from typing import Any, Dict, Tuple

class ValidationError(Exception):
    """Custom exception raised when game action validation fails."""
    pass

ALLOWED_ACTIONS = {"click", "keypress", "delay", "scroll"}
MAX_SCREEN_WIDTH = 3840
MAX_SCREEN_HEIGHT = 2160

def validate_action_type(action_type: str) -> None:
    """Ensures the action type is supported by the automation engine."""
    if action_type not in ALLOWED_ACTIONS:
        raise ValidationError(f"Invalid action type '{action_type}'. Must be one of {ALLOWED_ACTIONS}")

def validate_coordinates(coords: Tuple[int, int]) -> None:
    """Validates that the screen coordinates are within acceptable bounds."""
    if not isinstance(coords, (tuple, list)) or len(coords) != 2:
        raise ValidationError("Coordinates must be a tuple/list of two integers (x, y)")
    
    x, y = coords
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValidationError("Coordinate values must be integers")
        
    if not (0 <= x <= MAX_SCREEN_WIDTH) or not (0 <= y <= MAX_SCREEN_HEIGHT):
        raise ValidationError(f"Coordinates ({x}, {y}) out of screen bounds ({MAX_SCREEN_WIDTH}x{MAX_SCREEN_HEIGHT})")

def validate_delay(duration: float) -> None:
    """Validates the execution delay bounds to prevent hanging or negative values."""
    if not isinstance(duration, (int, float)):
        raise ValidationError("Delay duration must be a numerical value")
    if duration < 0 or duration > 60.0:
        raise ValidationError("Delay duration must be between 0 and 60 seconds")

def validate_game_action(payload: Dict[str, Any]) -> None:
    """Performs structural and value validation on incoming gaming actions."""
    if not isinstance(payload, dict):
        raise ValidationError("Action payload must be a dictionary")

    action_type = payload.get("type")
    if not action_type:
        raise ValidationError("Action payload is missing key: 'type'")

    validate_action_type(action_type)

    if action_type == "click":
        coords = payload.get("coords")
        if coords is None:
            raise ValidationError("Click action missing required 'coords' value")
        validate_coordinates(coords)

    elif action_type == "keypress":
        key = payload.get("key")
        if not key or not isinstance(key, str):
            raise ValidationError("Keypress action missing or invalid 'key' field")

    elif action_type == "delay":
        duration = payload.get("duration")
        if duration is None:
            raise ValidationError("Delay action missing required 'duration' value")
        validate_delay(duration)