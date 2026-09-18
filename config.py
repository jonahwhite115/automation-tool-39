import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "game_title": "Generic MMORPG",
    "target_fps": 60,
    "auto_loot": True,
    "keybinds": {
        "attack": "f1",
        "heal": "f2",
        "pause": "f12"
    },
    "detection_confidence": 0.85,
    "loop_delay_seconds": 0.1
}

class ConfigLoader:
    """Handles loading and saving game automation configuration with sensible defaults."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config: Dict[str, Any] = {}

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from file or creates it with defaults if missing."""
        if not os.path.exists(self.config_path):
            self.config = DEFAULT_CONFIG.copy()
            self.save_config()
            return self.config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
            
            self.config = DEFAULT_CONFIG.copy()
            self._recursive_update(self.config, user_config)
        except (json.JSONDecodeError, OSError):
            self.config = DEFAULT_CONFIG.copy()

        return self.config

    def _recursive_update(self, base_dict: Dict[str, Any], update_dict: Dict[str, Any]) -> None:
        """Recursively update nested dictionary structures."""
        for key, value in update_dict.items():
            if isinstance(value, dict) and key in base_dict and isinstance(base_dict[key], dict):
                self._recursive_update(base_dict[key], value)
            else:
                base_dict[key] = value

    def save_config(self) -> None:
        """Saves current configuration to JSON file."""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4)
