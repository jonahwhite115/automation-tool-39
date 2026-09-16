import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "vsync": True,
    "save_path": "./saves",
    "debug_mode": False
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads config from disk or returns defaults if missing."""
    if not os.path.exists(file_path):
        return DEFAULT_CONFIG

    try:
        with open(file_path, "r") as f:
            user_config = json.load(f)
            # Merge user config with defaults to ensure missing keys are present
            return {**DEFAULT_CONFIG, **user_config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any], file_path: str = "config.json") -> None:
    """Persists current configuration state to local json file."""
    try:
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")