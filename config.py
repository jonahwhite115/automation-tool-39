import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "auto_loot": True,
    "hotkey_profile": "default",
    "debug_mode": False
}

def load_configuration(filepath: str) -> Dict[str, Any]:
    """Loads configuration from JSON file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_data = json.load(f)
            # Update default values with user-provided settings
            config.update({k: v for k, v in user_data.items() if k in DEFAULT_CONFIG})
    except (json.JSONDecodeError, IOError):
        # In case of corruption, return established defaults
        pass
        
    return config

def save_configuration(filepath: str, config: Dict[str, Any]) -> None:
    """Persists current configuration state to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save config: {e}")