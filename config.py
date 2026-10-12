import os
from typing import Dict, Any

# Configuration settings for automation-tool-39
# Handles game environment paths and timing thresholds

DEFAULT_CONFIG = {
    "game_path": "C:\\Games\\TargetApp.exe",
    "check_interval": 5.0,
    "retry_attempts": 3,
    "log_level": "INFO"
}

def load_settings(path: str = "settings.json") -> Dict[str, Any]:
    """Loads configuration from external json if present."""
    if os.path.exists(path):
        try:
            import json
            with open(path, 'r') as f:
                return {**DEFAULT_CONFIG, **json.load(f)}
        except (IOError, ValueError):
            return DEFAULT_CONFIG
    return DEFAULT_CONFIG

class GameConfig:
    def __init__(self):
        self.settings = load_settings()
        self.game_path = self.settings.get("game_path")
        self.interval = self.settings.get("check_interval")

    def validate(self) -> bool:
        """Verify game path accessibility."""
        return os.path.exists(self.game_path) if self.game_path else False