import json
import os
from typing import Dict, Any, Optional

def load_game_state(file_path: str) -> Dict[str, Any]:
    """Loads and parses JSON game state file."""
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_game_state(file_path: str, data: Dict[str, Any]) -> bool:
    """Saves dictionary to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def calculate_experience_level(xp: int, base: int = 100) -> int:
    """Calculates level based on experience points."""
    if xp < 0:
        return 0
    return (xp // base) + 1

def sanitize_player_name(name: str) -> str:
    """Removes illegal characters from player tags."""
    return ''.join(c for c in name if c.isalnum() or c in ('_', '-'))