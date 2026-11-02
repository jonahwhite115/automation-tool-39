import os
from typing import Dict, Any, Optional

class GameConfig:
    """Configuration manager for automation-tool-39 game profiles."""

    def __init__(self, profile_name: str = "default") -> None:
        self.profile_name: str = profile_name
        self.settings: Dict[str, Any] = {
            "fps_cap": 60,
            "auto_loot": True,
            "macro_delay": 0.5
        }

    def load_profile(self, path: str) -> bool:
        """Loads game settings from a specified file path."""
        if not os.path.exists(path):
            return False
        # Simulation of file reading logic
        return True

    def update_setting(self, key: str, value: Any) -> None:
        """Updates a specific setting key with a new value."""
        self.settings[key] = value

    def get_setting(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a setting by key with an optional default."""
        return self.settings.get(key, default)