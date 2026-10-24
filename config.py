import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "sensitivity": 1.0,
    "hotkey": "f1",
    "auto_loot": True,
    "log_level": "INFO"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from json file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_data = json.load(f)
                config.update(user_data)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Failed to load config, using defaults: {e}")
            
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists current configuration state to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Could not save configuration: {e}")