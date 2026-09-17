import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_game": "Generic MMO",
    "fps_limit": 60,
    "scan_interval_ms": 100,
    "auto_loot": True,
    "keybindings": {
        "interact": "e",
        "use_potion": "q",
        "toggle_bot": "f9"
    },
    "detection_threshold": 0.85,
    "debug_mode": False
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Load configuration from a JSON file, falling back to defaults for missing keys."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                _deep_update(config, user_config)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: Failed to load {filepath} ({e}). Using defaults.")
    else:
        save_config(config, filepath)
        
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Save current configuration dictionary to a JSON file."""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    except OSError as e:
        print(f"Error: Could not save configuration to {filepath} ({e})")

def _deep_update(base_dict: Dict[str, Any], update_dict: Dict[str, Any]) -> None:
    """Recursively update dictionary to preserve nested default settings."""
    for key, value in update_dict.items():
        if isinstance(value, dict) and key in base_dict and isinstance(base_dict[key], dict):
            _deep_update(base_dict[key], value)
        else:
            base_dict[key] = value
