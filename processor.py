import logging
from typing import List, Dict, Any

# Configure logging for game automation tasks
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-39')

class GameStateProcessor:
    """Handles processing of raw game state data for automation logic."""

    def __init__(self, sensitivity: float = 1.0):
        self.sensitivity = sensitivity

    def clean_payload(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filters out stale or malformed state entries."""
        return [item for item in data if item.get('valid') and item.get('id')]

    def transform_coords(self, data: List[Dict[str, Any]]) -> List[Dict[str, float]]:
        """Normalizes coordinates for bot click precision."""
        results = []
        for entry in data:
            results.append({
                'x': entry['x'] * self.sensitivity,
                'y': entry['y'] * self.sensitivity,
                'action': entry.get('action', 'idle')
            })
        return results

    def process_frame(self, raw_data: List[Dict[str, Any]]) -> List[Dict[str, float]]:
        """Orchestrates the cleanup and transformation pipeline."""
        logger.info(f'Processing {len(raw_data)} entities')
        valid_data = self.clean_payload(raw_data)
        return self.transform_coords(valid_data)