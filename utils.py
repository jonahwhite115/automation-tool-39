import os
import logging
import shutil
from typing import List

logger = logging.getLogger('automation-tool-39')

def clear_temp_files(directory: str, extensions: List[str] = None) -> None:
    """Removes temporary cache and log files from gaming assets."""
    if extensions is None:
        extensions = ['.tmp', '.log', '.bak']
    
    if not os.path.exists(directory):
        logger.warning(f"Target directory {directory} does not exist.")
        return

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    logger.debug(f"Deleted: {file_path}")
                except OSError as e:
                    logger.error(f"Cleanup error on {file_path}: {e}")

def organize_assets(source: str, target: str) -> None:
    """Moves loose asset files into the structured target directory."""
    if not os.path.exists(target):
        os.makedirs(target)
    
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        if os.path.isfile(source_path):
            shutil.move(source_path, os.path.join(target, item))
            logger.info(f"Relocated asset: {item}")