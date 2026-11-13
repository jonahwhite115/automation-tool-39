import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "window_title": "Game Instance",
    "auto_click_interval": 0.5,
    "log_level": "INFO",
    "headless": False
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON or return defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(filepath):
        return config
        
    try:
        with open(filepath, "r") as f:
            user_data = json.load(f)
            config.update(user_data)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persist current configuration to disk."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)