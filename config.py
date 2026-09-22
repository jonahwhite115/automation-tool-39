import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "window_width": 1280,
    "window_height": 720,
    "frame_rate_cap": 60,
    "auto_login": False,
    "save_path": "./saves"
}

class ConfigLoader:
    def __init__(self, config_file: str = "settings.json"):
        self.config_file = config_file
        self.settings = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        """Loads existing configuration from disk or writes defaults."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    loaded_data = json.load(f)
                    self.settings.update(loaded_data)
            except (json.JSONDecodeError, IOError):
                self._save_defaults()
        else:
            self._save_defaults()

    def _save_defaults(self) -> None:
        """Persists current configuration state to disk."""
        try:
            with open(self.config_file, "w") as f:
                json.dump(self.settings, f, indent=4)
        except IOError as e:
            print(f"Failed to write config: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)