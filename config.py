import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "window_title": "Game Window",
    "auto_click_delay": 0.5,
    "log_level": "INFO",
    "max_retries": 3
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns default values."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(file_path):
        save_config(file_path, config)
        return config

    try:
        with open(file_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(file_path: str, config: Dict[str, Any]) -> None:
    """Persists current configuration state to disk."""
    with open(file_path, "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    # Initialize configuration file on first run
    settings = load_config()
    print(f"Loaded settings: {settings}")