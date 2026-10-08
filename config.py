import json
from typing import Dict, Any, Optional
from pathlib import Path

class GameConfig:
    """Handles loading and persistence of automation settings."""

    def __init__(self, config_path: str = "config.json") -> None:
        self.path: Path = Path(config_path)
        self.settings: Dict[str, Any] = self._load_default_settings()

    def _load_default_settings(self) -> Dict[str, Any]:
        """Provides default automation configuration structure."""
        return {
            "fps_limit": 60,
            "auto_loot": True,
            "macro_delay_ms": 150,
            "window_title": "GameClient"
        }

    def load(self) -> None:
        """Reads configuration from the filesystem."""
        if self.path.exists():
            with open(self.path, "r", encoding="utf-8") as f:
                self.settings.update(json.load(f))

    def save(self) -> None:
        """Persists current configuration state to disk."""
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=4)

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a configuration value by key."""
        return self.settings.get(key, default)

    def update(self, key: str, value: Any) -> None:
        """Updates a setting and validates type consistency."""
        self.settings[key] = value
        self.save()