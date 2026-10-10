import os
import logging
from pathlib import Path
from typing import List

# Configure logger for automation tasks
logger = logging.getLogger('automation-tool-39')

def get_game_directories(base_path: str) -> List[Path]:
    """Retrieve valid game installation directories."""
    root = Path(base_path)
    if not root.exists():
        logger.error(f"Path not found: {base_path}")
        return []
    
    return [d for d in root.iterdir() if d.is_dir() and (d / 'game.exe').exists()]

def cleanup_temp_files(directory: str, pattern: str = '*.tmp') -> int:
    """Remove temporary files to free up disk space."""
    count = 0
    path = Path(directory)
    
    for file in path.glob(pattern):
        try:
            file.unlink()
            count += 1
        except OSError as e:
            logger.warning(f"Failed to remove {file}: {e}")
            
    return count

def validate_game_config(config: dict, required_keys: List[str]) -> bool:
    """Verify all mandatory configuration keys exist."""
    return all(key in config for key in required_keys)