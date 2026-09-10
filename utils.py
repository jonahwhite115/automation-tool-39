import json
import os
from typing import Dict, Any, Optional

def load_game_data(file_path: str) -> Dict[str, Any]:
    """Load and parse local game configuration files."""
    if not os.path.exists(file_path):
        return {}
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_game_data(file_path: str, data: Dict[str, Any]) -> bool:
    """Atomic write operation for game state data."""
    try:
        temp_path = f"{file_path}.tmp"
        with open(temp_path, 'w') as f:
            json.dump(data, f, indent=4)
        os.replace(temp_path, file_path)
        return True
    except (IOError, TypeError):
        return False

def sanitize_player_name(name: str) -> str:
    """Strip non-alphanumeric characters from player identifiers."""
    return ''.join(char for char in name if char.isalnum())

def format_stats(stats: Dict[str, int]) -> str:
    """Convert dictionary stats to string display format."""
    return ", ".join([f"{k.capitalize()}: {v}" for k, v in stats.items()])