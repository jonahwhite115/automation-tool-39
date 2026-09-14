import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "auto_clicker": False,
    "log_level": "INFO",
    "window_mode": "borderless"
}

def load_config(filepath: str) -> Dict[str, Any]:
    """Loads config from json, merging with defaults."""
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
    """Persists current configuration state to disk."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)