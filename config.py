import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "resolution": "1920x1080",
    "enable_overlay": True,
    "log_level": "INFO"
}

def load_config(filepath: str) -> Dict[str, Any]:
    """Loads json configuration with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(filepath):
        return config
        
    try:
        with open(filepath, 'r') as f:
            user_data = json.load(f)
            config.update(user_data)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persists current configuration to disk."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)