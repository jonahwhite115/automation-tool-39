import json
import os
from typing import Any, Dict

def load_game_state(file_path: str) -> Dict[str, Any]:
    """Loads game state from a local JSON file."""
    if not os.path.exists(file_path):
        return {}
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_game_state(data: Dict[str, Any], file_path: str) -> bool:
    """Persists game state to a local JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def sanitize_player_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes invalid or empty entries from player stats."""
    return {k: v for k, v in data.items() if v is not None and v != ''}

def calculate_experience_modifier(level: int, base_mod: float) -> float:
    """Computes scaled experience multiplier based on level."""
    if level <= 0:
        return 1.0
    return base_mod * (1.0 + (level * 0.05))