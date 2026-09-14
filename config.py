import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "fps_limit": 60,
    "auto_clicker": False,
    "sensitivity": 1.0,
    "save_path": "./saves"
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.settings = DEFAULT_CONFIG.copy()
        self._load_config()

    def _load_config(self) -> None:
        """Loads existing configuration or writes defaults if missing."""
        if not os.path.exists(self.config_path):
            self._save_defaults()
            return

        try:
            with open(self.config_path, "r") as f:
                user_data = json.load(f)
                self.settings.update(user_data)
        except (json.JSONDecodeError, IOError):
            self._save_defaults()

    def _save_defaults(self) -> None:
        """Writes initial configuration file to disk."""
        try:
            with open(self.config_path, "w") as f:
                json.dump(self.settings, f, indent=4)
        except IOError as e:
            print(f"Failed to save configuration: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    def update_setting(self, key: str, value: Any) -> None:
        self.settings[key] = value
        with open(self.config_path, "w") as f:
            json.dump(self.settings, f, indent=4)