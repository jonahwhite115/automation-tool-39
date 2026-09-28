import os
import json
import logging

logger = logging.getLogger(__name__)

class ConfigManager:
    """Handles loading and validation of game automation settings."""

    def __init__(self, file_path='config.json'):
        self.file_path = file_path
        self.settings = {}

    def load_config(self):
        """Attempts to load configuration from disk with fallback."""
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"Configuration file {self.file_path} missing.")
            
            with open(self.file_path, 'r') as f:
                self.settings = json.load(f)
                
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Critical config error: {e}. Reverting to defaults.")
            self.settings = self._get_defaults()
        except Exception as e:
            logger.critical(f"Unexpected initialization failure: {e}")
            self.settings = self._get_defaults()
        
        return self.settings

    def _get_defaults(self):
        """Provides baseline safe settings for tool execution."""
        return {
            "fps_limit": 60,
            "auto_click": False,
            "macro_path": "./macros/default.json"
        }

def validate_settings(settings):
    """Ensures configuration values are within game-safe bounds."""
    if not isinstance(settings.get('fps_limit'), int):
        return False
    if not (1 <= settings.get('fps_limit', 0) <= 240):
        return False
    return True