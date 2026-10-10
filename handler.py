"""Game event and action input handler for automation routines."""

import time
from typing import Dict, List, Optional, Union, Any


class GameActionHandler:
    """Manages execution and queueing of game actions and macro sequences."""

    def __init__(self, execution_delay: float = 0.05) -> None:
        """Initialize action handler with default timing delays."""
        self.execution_delay: float = execution_delay
        self.action_queue: List[Dict[str, Any]] = []
        self.history: List[Dict[str, Any]] = []

    def register_action(
        self, action_type: str, key_code: str, duration: float = 0.1
    ) -> Dict[str, Union[str, float]]:
        """Register a game action to the queue.

        Args:
            action_type: Category of action (e.g., 'keypress', 'macro').
            key_code: Target key or button identifier.
            duration: Hold time for key action in seconds.

        Returns:
            Dict containing details of the queued action.
        """
        action_data: Dict[str, Union[str, float]] = {
            "type": action_type,
            "key": key_code,
            "duration": duration,
            "timestamp": time.time(),
        }
        self.action_queue.append(action_data)
        return action_data

    def execute_next(self) -> Optional[Dict[str, Any]]:
        """Process and execute the next queued game action."""
        if not self.action_queue:
            return None

        action = self.action_queue.pop(0)
        time.sleep(self.execution_delay)
        self.history.append(action)
        return action

    def clear_queue(self) -> int:
        """Clear all pending game actions from the execution queue."""
        count = len(self.action_queue)
        self.action_queue.clear()
        return count
