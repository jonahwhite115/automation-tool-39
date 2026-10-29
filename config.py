import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "window_width": 1920,
    "window_height": 1080,
    "fps_limit": 144,
    "auto_login": True,
    "log_level": "INFO"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Config load error: {e}. Using defaults.")

    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """Persists current configuration state to disk."""
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Config save error: {e}")