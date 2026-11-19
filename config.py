import os
import json
import logging

class ConfigManager:
    """Handles loading and validation of gaming automation settings."""
    
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.defaults = {"resolution": [1920, 1080], "sensitivity": 1.0}

    def load_config(self) -> dict:
        """Loads configuration with fallback for missing or corrupted files."""
        if not os.path.exists(self.config_path):
            logging.warning("Config file not found, creating defaults")
            return self.defaults

        try:
            with open(self.config_path, 'r') as f:
                data = json.load(f)
                if not isinstance(data, dict):
                    raise ValueError("Config must be a JSON object")
                return {**self.defaults, **data}
        except (json.JSONDecodeError, ValueError, IOError) as e:
            logging.error(f"Failed to load config: {e}. Reverting to defaults.")
            return self.defaults

    def save_config(self, data: dict) -> bool:
        """Persists configuration safely to disk."""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except (TypeError, PermissionError, IOError) as e:
            logging.error(f"Critical write failure: {e}")
            return False