import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "auto_clicker": False,
    "hotkey": "f10",
    "logging": True
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults if missing."""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            config = json.load(f)
            # Ensure defaults for missing keys
            return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists current configuration to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    current_config = load_config()
    print(f"Active configuration: {current_config}")