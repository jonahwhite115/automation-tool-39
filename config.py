import os
from pathlib import Path
from typing import Dict, Any

# Project path constants for automation-tool-39
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"

# Configuration dictionary for game automation parameters
SETTINGS: Dict[str, Any] = {
    "max_retries": 3,
    "polling_interval": 0.5,
    "headless_mode": True,
    "target_game": "automation-tool-39-client",
    "auto_save": True,
    "resolution": (1920, 1080),
}

def setup_environment() -> None:
    """Ensures necessary directories exist for tool runtime."""
    for directory in [LOG_DIR, DATA_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

def get_setting(key: str, default: Any = None) -> Any:
    """Retrieves a setting with a fallback mechanism."""
    return SETTINGS.get(key, default)

# Initialize environment paths on module import
setup_environment()