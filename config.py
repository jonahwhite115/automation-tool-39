import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "auto_clicker": False,
    "macro_delay": 500,
    "theme": "dark"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults."""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            config = json.load(f)
            return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists configuration to a JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save config: {e}")

if __name__ == "__main__":
    # Example usage for gaming tool initialization
    current_config = load_config()
    print(f"Loaded configuration: {current_config}")