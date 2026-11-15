import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "sensitivity": 1.5,
    "polling_rate": 60,
    "auto_clicker": False,
    "hotkey": "F8"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration with default fallback values."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(filepath):
        _save_config(filepath, config)
        return config

    try:
        with open(filepath, "r") as f:
            user_data = json.load(f)
            config.update(user_data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def _save_config(filepath: str, data: Dict[str, Any]) -> None:
    """Persists current configuration to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
    except IOError:
        pass