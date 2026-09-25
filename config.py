import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "screen_resolution": [1920, 1080],
    "click_delay_ms": 100,
    "max_retries": 3,
    "debug_mode": False,
    "keybinds": {
        "start": "F10",
        "stop": "F11",
        "pause": "F12"
    },
    "target_game": "Default_RPG"
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Loads configuration file, merging with default values."""
        if not os.path.exists(self.filepath):
            self._save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                user_config = json.load(f)
            
            # Merge loaded configurations with the defaults
            merged = DEFAULT_CONFIG.copy()
            for key, value in user_config.items():
                if isinstance(value, dict) and key in merged and isinstance(merged[key], dict):
                    merged[key].update(value)
                else:
                    merged[key] = value
            return merged
        except (json.JSONDecodeError, IOError):
            # Fallback to default copy in case of read errors
            return DEFAULT_CONFIG.copy()

    def _save_config(self, data: Dict[str, Any]) -> None:
        """Helper to persist configuration data to a file."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except IOError:
            pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by its key."""
        return self.config.get(key, default)

    def update_key(self, key: str, value: Any) -> None:
        """Updates a config setting and immediately persists it to disk."""
        self.config[key] = value
        self._save_config(self.config)
