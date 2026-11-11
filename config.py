import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "resolution": "1920x1080",
    "fps_cap": 60,
    "auto_save": True,
    "retry_limit": 3
}

def load_configuration(filepath: str) -> Dict[str, Any]:
    """
    loads json config from disk or returns defaults
    """
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG.copy()

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            # merge defaults with user input
            config = DEFAULT_CONFIG.copy()
            config.update(user_config)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_configuration(filepath: str, config: Dict[str, Any]) -> bool:
    """
    persists current config dictionary to json
    """
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False