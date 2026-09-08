import logging
from typing import List, Dict

class GameDataProcessor:
    """Handles raw game telemetry data cleanup and normalization."""

    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def sanitize_stats(self, raw_data: List[Dict]) -> List[Dict]:
        """Filters invalid entries and ensures score consistency."""
        cleaned = []
        for entry in raw_data:
            if self._is_valid(entry):
                entry['score'] = max(0, entry.get('score', 0))
                cleaned.append(entry)
            else:
                self.logger.warning(f"Skipping malformed entry: {entry}")
        return cleaned

    def _is_valid(self, entry: Dict) -> bool:
        """Validates player session dictionary structure."""
        required = ['player_id', 'session_id']
        return all(key in entry for key in required)

    def aggregate_sessions(self, data: List[Dict]) -> Dict[str, float]:
        """Calculates average session duration per player."""
        totals: Dict[str, List[float]] = {}
        for entry in data:
            pid = entry['player_id']
            totals.setdefault(pid, []).append(entry.get('duration', 0))
        
        return {pid: sum(durs) / len(durs) for pid, durs in totals.items()}