import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "auto_loot": True,
    "macro_delay": 0.5,
    "window_name": "GameWindow"
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from JSON file or returns default."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def save_config(config: Dict[str, Any], file_path: str = "config.json") -> None:
    """Persists current configuration state to disk."""
    try:
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError:
        pass