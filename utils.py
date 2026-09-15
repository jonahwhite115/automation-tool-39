import time
from typing import List, Optional, Dict

class GameStateUtils:
    """Utility functions for managing game automation states."""

    def __init__(self, session_id: str) -> None:
        self.session_id: str = session_id
        self.start_time: float = time.time()

    def format_coordinates(self, x: float, y: float) -> Dict[str, float]:
        """Normalize coordinates for game engine input."""
        return {"x": round(x, 2), "y": round(y, 2)}

    def calculate_uptime(self) -> float:
        """Calculate current session duration in seconds."""
        return round(time.time() - self.start_time, 2)

    @staticmethod
    def validate_action_queue(queue: List[str]) -> bool:
        """Check if the action queue contains valid game commands."""
        valid_commands = {"move", "click", "wait", "loot"}
        return all(cmd in valid_commands for cmd in queue)

    def get_session_metadata(self) -> Dict[str, Optional[str]]:
        """Return dictionary containing session details."""
        return {
            "id": self.session_id,
            "duration": f"{self.calculate_uptime()}s",
            "status": "active"
        }