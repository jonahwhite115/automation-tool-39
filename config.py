import os
from typing import Dict, Any

class GameConfig:
    """Central configuration management for automation-tool-39."""
    def __init__(self) -> None:
        self.settings: Dict[str, Any] = {
            "resolution": (1920, 1080),
            "fps_limit": 60,
            "auto_loot": True,
            "macro_delay": 0.5
        }
        self._load_env_overrides()

    def _load_env_overrides(self) -> None:
        """Apply environment variables to settings if present."""
        for key in self.settings.keys():
            env_val = os.getenv(f"GAMETOOL_{key.upper()}")
            if env_val:
                self.settings[key] = type(self.settings[key])(env_val)

    def get(self, key: str) -> Any:
        return self.settings.get(key)

    def update(self, key: str, value: Any) -> None:
        if key in self.settings:
            self.settings[key] = value

# Global instance for tool-wide access
config = GameConfig()