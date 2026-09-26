import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "screen_resolution": [1920, 1080],
    "click_delay_seconds": 0.1,
    "keybind_start": "F9",
    "keybind_stop": "F12",
    "active_profile": "default_rpg",
    "retry_attempts": 3,
    "verbose_logging": False
}

class ConfigLoader:
    """Handles loading, merging, and saving configuration for the gaming automation tool."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads config from file, merging with defaults for any missing keys."""
        merged_config = DEFAULT_CONFIG.copy()

        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as file:
                    user_config = json.load(file)
                    if isinstance(user_config, dict):
                        merged_config.update(user_config)
            except (json.JSONDecodeError, OSError):
                # Fallback to defaults on corrupted or unreadable configuration file
                pass
        else:
            self.save_config(merged_config)

        return merged_config

    def save_config(self, config_data: Dict[str, Any]) -> None:
        """Saves the configuration dictionary to the designated file path."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as file:
                json.dump(config_data, file, indent=4)
        except OSError:
            pass

    def get(self, key: str) -> Any:
        """Retrieves a configuration value by its key with fallback safety."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))