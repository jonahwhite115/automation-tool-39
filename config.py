import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "game_path": "C:/Games/Title",
    "auto_click_interval": 0.5,
    "log_level": "INFO",
    "enable_overlay": True
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback to defaults."""
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
    """Persists current configuration state to disk."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    current_cfg = load_config()
    print(f"Active configuration: {current_cfg}")