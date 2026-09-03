import re
from typing import Dict, Any, Tuple

class ValidationError(Exception):
    """Exception raised for errors in the input validation."""
    pass

def validate_game_action(payload: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Validates gaming action inputs for the automation loop.
    Ensures coordinates are within screen boundaries and actions are allowed.
    """
    allowed_actions = {"click", "keypress", "drag", "wait"}
    
    action = payload.get("action")
    if not action or action not in allowed_actions:
        return False, f"Invalid action: {action}. Must be one of {allowed_actions}"
        
    if action in ("click", "drag"):
        coords = payload.get("coords")
        if not isinstance(coords, (list, tuple)) or len(coords) != 2:
            return False, "Coordinates must be a list or tuple of (x, y)"
        x, y = coords
        if not (isinstance(x, int) and isinstance(y, int)):
            return False, "Coordinates must be integers"
        if x < 0 or y < 0 or x > 1920 or y > 1080:
            return False, "Coordinates out of bounds (0-1920, 0-1080)"
            
    if action == "keypress":
        key = payload.get("key")
        if not isinstance(key, str) or len(key) == 0:
            return False, "Key must be a non-empty string"
        if not re.match(r"^[a-zA-Z0-9_]+$", key):
            return False, "Invalid key format"
            
    if action == "wait":
        duration = payload.get("duration")
        if not isinstance(duration, (int, float)) or duration <= 0:
            return False, "Wait duration must be a positive number"
            
    return True, "Valid action"