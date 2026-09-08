import json
import os
from typing import Dict, Any, Optional

def load_game_state(file_path: str) -> Dict[str, Any]:
    """Loads and validates JSON game state files."""
    if not os.path.exists(file_path):
        return {}
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, IOError):
        return {}

def save_game_state(file_path: str, data: Dict[str, Any]) -> bool:
    """Serializes game state dictionary to JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def get_stat_value(data: Dict[str, Any], key: str, default: int = 0) -> int:
    """Extracts integer statistics with fallback default."""
    return int(data.get(key, default))

def update_player_level(data: Dict[str, Any], xp: int) -> Dict[str, Any]:
    """Calculates level based on experience points."""
    data['level'] = (xp // 1000) + 1
    data['xp'] = xp
    return data