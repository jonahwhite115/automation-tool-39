import json
import os
from typing import Dict, Any, Optional

def load_game_data(file_path: str) -> Dict[str, Any]:
    """Loads and parses JSON game configuration files."""
    if not os.path.exists(file_path):
        return {}
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_game_data(file_path: str, data: Dict[str, Any]) -> bool:
    """Serializes game data dictionary to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def sanitize_player_stats(stats: Dict[str, Any]) -> Dict[str, int]:
    """Ensures all numerical statistics are integers."""
    cleaned = {}
    for key, value in stats.items():
        try:
            cleaned[key] = int(value)
        except (ValueError, TypeError):
            cleaned[key] = 0
    return cleaned

def get_session_id(player_name: str, server_id: str) -> str:
    """Generates a unique session string for logging."""
    return f"{server_id}_{player_name.lower().replace(' ', '_')}"