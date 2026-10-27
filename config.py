import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "game_path": "C:/Games/bin/client.exe",
    "refresh_rate": 60,
    "auto_clicker_enabled": False,
    "log_level": "INFO"
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from json file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not parse {file_path}, using defaults")
            
    return config

def save_config(config: Dict[str, Any], file_path: str = "config.json") -> None:
    """Persists current configuration state to disk."""
    try:
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error saving configuration: {e}")