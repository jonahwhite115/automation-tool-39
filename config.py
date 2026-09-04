import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "window_width": 1920,
    "window_height": 1080,
    "fps_limit": 60,
    "enable_logging": True,
    "auto_save_path": "./saves"
}

class ConfigLoader:
    """Handles loading and merging of game configuration files."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path

    def load(self) -> Dict[str, Any]:
        """Loads config from disk or returns defaults if missing."""
        if not os.path.exists(self.config_path):
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
                # Deep merge defaults with user overrides
                return {**DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG.copy()

    def save(self, config_data: Dict[str, Any]) -> None:
        """Persists current configuration to file."""
        with open(self.config_path, "w") as f:
            json.dump(config_data, f, indent=4)