import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class GameStateProcessor:
    def __init__(self, data_stream: List[Dict[str, Any]]):
        self.data_stream = data_stream

    def sanitize_input(self) -> List[Dict[str, Any]]:
        """Removes invalid or empty gaming event packets."""
        return [item for item in self.data_stream if item and 'event_id' in item]

    def process_events(self) -> List[str]:
        """Normalizes and categorizes raw game events."""
        sanitized = self.sanitize_input()
        processed_results = []

        for event in sanitized:
            try:
                event_type = event.get('type', 'unknown')
                event_id = event['event_id']
                processed_results.append(f"{event_type}_{event_id}")
            except KeyError as e:
                logger.error(f"failed to parse event structure: {e}")

        return processed_results

    def run_cleanup(self):
        """Clears memory buffer after batch processing."""
        self.data_stream.clear()
        logger.info("buffer cleared successfully")