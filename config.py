import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_fps": 60,
    "scan_interval_ms": 100,
    "hotkeys": {
        "start": "f10",
        "stop": "f11",
        "screenshot": "f12"
    },
    "detection_threshold": 0.85,
    "game_window_title": "GameClient",
    "debug_mode": False
}

class ConfigLoader:
    """Loads and manages gaming automation configuration with default fallback values."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        """Loads configuration from file and merges it with defaults."""
        if not os.path.exists(self.config_path):
            self.save()  # Create default config file if it does not exist
            return

        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    self._merge_dicts(self.config, user_config)
        except (json.JSONDecodeError, OSError):
            # Falls back to default on parse or read errors
            pass

    def _merge_dicts(self, base: Dict[str, Any], update: Dict[str, Any]) -> None:
        """Recursively merges custom updates into the base configuration."""
        for key, val in update.items():
            if isinstance(val, dict) and key in base and isinstance(base[key], dict):
                self._merge_dicts(base[key], val)
            else:
                base[key] = val

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a nested or top-level configuration value."""
        return self.config.get(key, default)

    def save(self) -> None:
        """Persists current configuration state to disk."""
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4)
        except OSError:
            pass