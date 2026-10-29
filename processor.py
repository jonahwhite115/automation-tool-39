from typing import List, Dict, Optional

class GameStateProcessor:
    """Handles processing of raw game memory state for automation."""

    def __init__(self, buffer_size: int = 1024) -> None:
        """Initialize the processor with a specific memory buffer size."""
        self.buffer_size: int = buffer_size
        self.history: List[Dict[str, float]] = []

    def parse_entities(self, raw_data: bytes) -> List[Dict[str, float]]:
        """Parse binary stream into structured entity data."""
        if not raw_data:
            return []
            
        # Mock parsing logic
        return [{"id": 1.0, "x": 10.5, "y": 20.3}]

    def filter_active_players(self, entities: List[Dict[str, float]]) -> List[Dict[str, float]]:
        """Extract only players currently in the active session."""
        return [e for e in entities if e.get("id", 0) > 0]

    def update_metrics(self, data: List[Dict[str, float]]) -> None:
        """Append new state data to the internal history log."""
        if len(self.history) > self.buffer_size:
            self.history.pop(0)
        self.history.extend(data)

    def get_latest_position(self) -> Optional[Dict[str, float]]:
        """Retrieve the most recent entity position from history."""
        return self.history[-1] if self.history else None