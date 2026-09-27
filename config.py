import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "window_width": 1920,
    "window_height": 1080,
    "polling_rate_ms": 50,
    "debug_mode": False,
    "target_process": "game.exe"
}

class ConfigLoader:
    """Handles loading and merging of automation tool settings."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path

    def load(self) -> Dict[str, Any]:
        """Loads config from file with fallback to defaults."""
        if not os.path.exists(self.config_path):
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
            
            # Merge defaults with user settings
            config = DEFAULT_CONFIG.copy()
            config.update(user_config)
            return config
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG.copy()

    def save(self, config: Dict[str, Any]) -> None:
        """Persists current configuration state to disk."""
        with open(self.config_path, "w") as f:
            json.dump(config, f, indent=4)