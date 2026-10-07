import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "fps_limit": 144,
    "auto_start": True,
    "log_level": "INFO",
    "window_mode": "borderless"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults if missing."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: failed to load config file: {e}. Using defaults.")

    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> bool:
    """Persists current configuration to JSON file."""
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
        return True
    except IOError as e:
        print(f"Error: could not save config: {e}")
        return False