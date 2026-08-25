import re
from typing import Any, Dict, List

def validate_player_name(name: Any) -> str:
    """Validate player name for edge cases like empty, short, long and invalid chars."""
    if not isinstance(name, str):
        raise ValueError("Player name must be a string")
    name = name.strip()
    if not name:
        raise ValueError("Player name cannot be empty")
    if len(name) < 3:
        raise ValueError("Player name must be at least 3 characters long")
    if len(name) > 16:
        raise ValueError("Player name cannot exceed 16 characters")
    if not re.match(r"^[a-zA-Z0-9_]+$", name):
        raise ValueError("Player name must contain only alphanumeric and underscores")
    return name

def validate_game_mode(mode: Any, allowed: List[str]) -> str:
    """Validate game mode with type and value edge case handling."""
    if not isinstance(mode, str):
        raise ValueError("Game mode must be a string")
    mode = mode.strip().lower()
    if not mode:
        raise ValueError("Game mode cannot be empty")
    if mode not in [m.lower() for m in allowed]:
        raise ValueError(f"Invalid game mode. Allowed: {', '.join(allowed)}")
    return mode

def validate_score(score: Any) -> int:
    """Validate score with conversion error handling and range checks."""
    try:
        score = int(score)
    except (ValueError, TypeError):
        raise ValueError("Score must be an integer")
    if score < 0:
        raise ValueError("Score cannot be negative")
    if score > 999999:
        raise ValueError("Score exceeds max limit")
    return score

def validate_player_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate player data with error collection for multiple edge cases."""
    if not isinstance(data, dict):
        raise ValueError("Player data must be a dictionary")
    if not data:
        raise ValueError("Player data cannot be empty")
    validated: Dict[str, Any] = {}
    errors: List[str] = []
    if "name" not in data:
        errors.append("name is required")
    else:
        try:
            validated["name"] = validate_player_name(data["name"])
        except ValueError as e:
            errors.append(str(e))
    allowed = ["solo", "duo", "squad"]
    if "mode" not in data:
        errors.append("mode is required")
    else:
        try:
            validated["mode"] = validate_game_mode(data["mode"], allowed)
        except ValueError as e:
            errors.append(str(e))
    if "score" in data:
        try:
            validated["score"] = validate_score(data["score"])
        except ValueError as e:
            errors.append(str(e))
    if errors:
        raise ValueError("Validation failed: " + "; ".join(errors))
    return validated