import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "window_width": 1280,
    "window_height": 720,
    "target_fps": 60,
    "auto_save_interval": 300,
    "debug_mode": False
}

def load_config(filepath: str) -> Dict[str, Any]:
    """Loads config from disk, merging with defaults."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persists current configuration to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)