import logging
import os
from typing import Optional

# Logging configuration for automation-tool-39
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('automation-tool-39')

def validate_path(path: str) -> bool:
    """Verify file system access for game assets."""
    return os.path.exists(path) and os.access(path, os.R_OK)

def get_environment_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieve system settings with fallback."""
    value = os.getenv(key, default)
    if not value:
        logger.warning(f"Missing expected environment variable: {key}")
    return value or ""

def format_game_timestamp(raw_time: float) -> str:
    """Convert engine time into human readable format."""
    seconds = int(raw_time % 60)
    minutes = int((raw_time // 60) % 60)
    hours = int(raw_time // 3600)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def clean_cache_directory(dir_path: str) -> None:
    """Removal of temporary game artifact files."""
    try:
        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
        logger.info(f"Cache cleared at {dir_path}")
    except OSError as e:
        logger.error(f"Failed to clean cache: {e}")