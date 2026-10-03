import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class GameConfig:
    POLLING_RATE: float = 0.5
    MAX_RETRIES: int = 3
    SESSION_TIMEOUT: int = 3600
    DEFAULT_LOG_LEVEL: str = 'INFO'

class ConfigLoader:
    """Handles configuration ingestion from environment variables."""
    def __init__(self) -> None:
        self._defaults = GameConfig()

    def get_setting(self, key: str, default: Any = None) -> Any:
        return os.getenv(key, default or getattr(self._defaults, key, None))

    @property
    def settings(self) -> Dict[str, Any]:
        return {
            "rate": self.get_setting("POLLING_RATE"),
            "retries": self.get_setting("MAX_RETRIES"),
            "timeout": self.get_setting("SESSION_TIMEOUT")
        }

def load_config() -> ConfigLoader:
    return ConfigLoader()