import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "window_title": "Game Client",
    "fps_limit": 60,
    "auto_clicker_enabled": False,
    "click_interval_ms": 500
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk, falling back to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(file_path):
        _save_default_config(file_path, config)
        return config
        
    try:
        with open(file_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        # Fallback to defaults on corrupted file
        pass
        
    return config

def _save_default_config(file_path: str, config: Dict[str, Any]) -> None:
    """Initializes configuration file with default values."""
    try:
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError:
        pass