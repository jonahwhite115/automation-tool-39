import json
import os
from typing import Any, Dict, Optional

def load_game_data(file_path: str) -> Dict[str, Any]:
    """Load and parse game configuration or save data."""
    if not os.path.exists(file_path):
        return {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_game_data(file_path: str, data: Dict[str, Any]) -> bool:
    """Persist game state to a json file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_player_stats(stats: Dict[str, Any], required_keys: list) -> bool:
    """Verification of player stat integrity."""
    return all(key in stats for key in required_keys)

def sanitize_input(user_input: str) -> str:
    """Basic sanitization for gaming console commands."""
    return str(user_input).strip().lower()