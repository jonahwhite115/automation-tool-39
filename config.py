import json
import os
from typing import Dict, Any, Tuple


class ConfigError(Exception):
    """Raised when there is an issue loading or validating configuration."""

    pass


class GameConfig:
    """Manages the configuration settings for the gaming automation tool.

    Handles loading from disk, validation of keys, and default values
    for automation parameters like resolution and hotkeys.
    """

    DEFAULT_CONFIG: Dict[str, Any] = {
        "window_title": "Mortal Kombat 11",
        "resolution": [1920, 1080],
        "target_fps": 60,
        "confidence_threshold": 0.85,
        "hotkeys": {"start": "f1", "stop": "f2"},
    }

    def __init__(self, filepath: str) -> None:
        """Initializes config manager and loads setting file if it exists."""
        self.filepath: str = filepath
        self.settings: Dict[str, Any] = self.DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        """Loads configuration from JSON file; creates it with defaults if missing."""
        if not os.path.exists(self.filepath):
            self.save()
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                user_data = json.load(file)
                self._merge_and_validate(user_data)
        except (json.JSONDecodeError, OSError) as error:
            raise ConfigError(
                f"Failed to read config file: {error}"
            ) from error

    def save(self) -> None:
        """Saves current settings dict to the configuration file."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(self.settings, file, indent=4)
        except OSError as error:
            raise ConfigError(
                f"Failed to save config file: {error}"
            ) from error

    def _merge_and_validate(self, data: Dict[str, Any]) -> None:
        """Validates and merges user settings over the default values."""
        for key, value in data.items():
            if key in self.DEFAULT_CONFIG:
                if not isinstance(value, type(self.DEFAULT_CONFIG[key])):
                    raise ConfigError(
                        f"Invalid type for {key}: expected {type(self.DEFAULT_CONFIG[key])}"
                    )
                self.settings[key] = value

    @property
    def resolution_tuple(self) -> Tuple[int, int]:
        """Returns resolution configuration as a width/height integer tuple."""
        res = self.settings["resolution"]
        return (res[0], res[1])
