from typing import Any, Dict, List, Optional, Tuple


def validate_game_action(payload: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """Validates incoming action payloads before processing in the main loop."""
    if not isinstance(payload, dict):
        return False, "Payload must be a dictionary"

    action_type = payload.get("action_type")
    if not action_type or not isinstance(action_type, str):
        return False, "Missing or invalid 'action_type'"

    allowed_actions = {"click", "key_press", "delay", "move"}
    if action_type not in allowed_actions:
        return False, f"Unsupported action type: {action_type}"

    if action_type in {"click", "move"}:
        coords = payload.get("coordinates")
        if not isinstance(coords, (list, tuple)) or len(coords) != 2:
            return False, "Coordinates must be a 2-element tuple or list"
        x, y = coords
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            return False, "Coordinates must contain numeric values"
        if x < 0 or y < 0:
            return False, "Coordinates cannot be negative"

    if action_type == "delay":
        duration = payload.get("duration")
        if not isinstance(duration, (int, float)) or duration < 0:
            return False, "Delay duration must be a non-negative number"

    return True, None


def sanitize_input_queue(raw_queue: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filters out invalid action items from an incoming input processing queue."""
    valid_commands = []
    for item in raw_queue:
        is_valid, _ = validate_game_action(item)
        if is_valid:
            valid_commands.append(item)
    return valid_commands
