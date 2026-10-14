import os
from typing import Dict, Any

# Gaming automation tool configurations
DEFAULT_SETTINGS: Dict[str, Any] = {
    "screen_resolution": (1920, 1080),
    "scan_interval": 0.5,
    "debug_mode": False,
    "log_level": "INFO",
    "retry_attempts": 3
}

def get_env_var(key: str, default: Any = None) -> Any:
    """Retrieve environment variables with fallback defaults."""
    return os.getenv(key, default)

class AppConfig:
    def __init__(self) -> None:
        self.settings = DEFAULT_SETTINGS.copy()
        self._load_environment_overrides()

    def _load_environment_overrides(self) -> None:
        """Update settings from environment variables if present."""
        env_val = get_env_var("DEBUG_MODE")
        if env_val is not None:
            self.settings["debug_mode"] = env_val.lower() == "true"

        scan_rate = get_env_var("SCAN_INTERVAL")
        if scan_rate:
            self.settings["scan_interval"] = float(scan_rate)

    def get(self, key: str) -> Any:
        return self.settings.get(key)

config = AppConfig()