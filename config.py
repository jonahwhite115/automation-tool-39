import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "auto_clicker": False,
    "keybinds": {
        "macro": "F8",
        "toggle": "F9"
    }
}

class ConfigLoader:
    """Handles loading and merging of application settings."""
    
    def __init__(self, config_path: str = "config.json"):
        self.path = config_path

    def load(self) -> Dict[str, Any]:
        """Loads config from file, falls back to defaults if missing."""
        if not os.path.exists(self.path):
            self._save_defaults()
            return DEFAULT_CONFIG
            
        try:
            with open(self.path, "r") as f:
                user_config = json.load(f)
            return {**DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG

    def _save_defaults(self) -> None:
        """Persists default configuration to disk."""
        try:
            with open(self.path, "w") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
        except IOError as e:
            print(f"Failed to write default config: {e}")