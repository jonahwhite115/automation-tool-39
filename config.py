import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "auto_clicker_enabled": False,
    "hotkey": "F8",
    "save_path": "./saves"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from file with fallback to defaults.
    """
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load {filepath}, using defaults. Error: {e}")

    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """
    Persists configuration dictionary to file.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error: Could not save configuration to {filepath}. {e}")

if __name__ == "__main__":
    # Example usage for automation-tool-39 initialization
    current_config = load_config()
    print(f"Active Configuration: {current_config}")