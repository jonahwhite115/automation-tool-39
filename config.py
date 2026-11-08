import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "resolution": [1920, 1080],
    "auto_clicker": False,
    "log_level": "INFO"
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults if file missing."""
    if not os.path.exists(path):
        save_config(DEFAULT_CONFIG, path)
        return DEFAULT_CONFIG

    try:
        with open(path, "r") as f:
            config = json.load(f)
            # Merge loaded config with defaults to ensure missing keys are present
            return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any], path: str = "config.json") -> None:
    """Persists configuration dictionary to a JSON file."""
    try:
        with open(path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")