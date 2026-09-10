import json
import os
from typing import Dict, Any, Optional

def load_game_data(file_path: str) -> Dict[str, Any]:
    """Loads gaming JSON configuration or stats file."""
    if not os.path.exists(file_path):
        return {}
    
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return {}

def save_game_data(file_path: str, data: Dict[str, Any]) -> bool:
    """Persists game state to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except IOError:
        return False

def get_stat(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    """Retrieves nested stat safely from dictionary."""
    keys = key.split('.')
    val = data
    for k in keys:
        if isinstance(val, dict):
            val = val.get(k)
        else:
            return default
    return val if val is not None else default