import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "window_width": 1280,
    "window_height": 720,
    "fps_limit": 60,
    "auto_clicker_enabled": False,
    "macro_delay": 0.5
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from JSON file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(filepath):
        return config
        
    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists current configuration dictionary to disk."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)