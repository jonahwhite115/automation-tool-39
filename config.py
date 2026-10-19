import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "resolution": "1920x1080",
    "fps_limit": 60,
    "auto_loot": True,
    "log_level": "INFO"
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(path):
        return config

    try:
        with open(path, "r") as f:
            user_data = json.load(f)
            config.update(user_data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(config: Dict[str, Any], path: str = "config.json") -> None:
    """Persists current configuration to json file."""
    with open(path, "w") as f:
        json.dump(config, f, indent=4)