import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "sensitivity": 1.0,
    "polling_rate": 60,
    "auto_save": True,
    "log_level": "INFO"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from JSON file with defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            print(f"Failed to load {filepath}, using defaults")
            
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists current configuration to JSON."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error saving config: {e}")