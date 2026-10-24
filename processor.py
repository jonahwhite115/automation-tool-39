import os
import logging
from typing import List

# Configure gaming process logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-39')

class GameProcessor:
    def __init__(self, target_dir: str):
        self.target_dir = target_dir
        self.cache_ext = '.tmp'

    def cleanup_temp_files(self) -> int:
        """Removes cached gaming artifacts to free storage."""
        removed_count = 0
        if not os.path.exists(self.target_dir):
            return 0

        for root, _, files in os.walk(self.target_dir):
            for file in files:
                if file.endswith(self.cache_ext):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    removed_count += 1
        
        logger.info(f'Cleaned {removed_count} temporary gaming files')
        return removed_count

    def reorganize_assets(self, target_folders: List[str]) -> None:
        """Consolidates assets into directory structure."""
        for folder in target_folders:
            path = os.path.join(self.target_dir, folder)
            if not os.path.exists(path):
                os.makedirs(path)
                logger.info(f'Created category directory: {folder}')