import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "game_path": "C:\\Games\\AutomationGame",
    "auto_click_interval": 0.5,
    "log_level": "INFO",
    "enable_overlay": True
}

class ConfigLoader:
    """Handles loading and merging of application configuration."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.data = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Loads config from file if it exists, otherwise returns defaults."""
        if not os.path.exists(self.config_path):
            self._save_defaults()
            return self.data

        try:
            with open(self.config_path, 'r') as f:
                user_data = json.load(f)
                self.data.update(user_data)
        except (json.JSONDecodeError, IOError):
            # Revert to safe defaults on corruption
            pass
            
        return self.data

    def _save_defaults(self) -> None:
        """Persists default configuration to the specified path."""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
        except IOError:
            pass

if __name__ == "__main__":
    loader = ConfigLoader()
    current_cfg = loader.load()
    print(f"Active config: {current_cfg}")