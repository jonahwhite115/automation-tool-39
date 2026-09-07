import os
import logging
from pathlib import Path
from typing import List

# Configure standard logger for automation tasks
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('automation-tool-39')

def get_game_files(directory: str, extension: str = '.sav') -> List[Path]:
    """Retrieve list of game save files from specified directory."""
    path = Path(directory)
    if not path.exists():
        logger.error(f"Directory {directory} does not exist")
        return []
    return list(path.glob(f'*{extension}'))

def cleanup_old_backups(directory: str, max_files: int = 5) -> None:
    """Maintain limited count of backups to conserve storage."""
    files = sorted(
        [f for f in Path(directory).iterdir() if f.is_file()],
        key=os.path.getmtime
    )
    
    if len(files) > max_files:
        to_delete = files[:-max_files]
        for file in to_delete:
            file.unlink()
            logger.info(f"Removed stale backup: {file.name}")

def validate_path(path: str) -> bool:
    """Ensure provided path is a directory for automation."""
    return Path(path).is_dir()