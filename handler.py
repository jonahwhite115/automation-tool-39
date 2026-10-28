"""Game event handler module for processing automated in-game actions."""

import time
from typing import Any, Dict, List, Optional


class GameEventHandler:
    """Processes and executes automated game macros and event sequences."""

    def __init__(self, target_window: str, cooldown: float = 0.5) -> None:
        """Initialize the handler with target window name and default action cooldown."""
        self.target_window: str = target_window
        self.cooldown: float = cooldown
        self.history: List[Dict[str, Any]] = []

    def execute_action(self, action_type: str, payload: Dict[str, Any]) -> bool:
        """Execute a specific gaming action macro.

        Args:
            action_type: Name of the action command (e.g., 'cast_spell', 'use_item').
            payload: Parameters required for action execution.

        Returns:
            True if execution succeeded, False otherwise.
        """
        if not action_type or not isinstance(payload, dict):
            return False

        timestamp: float = time.time()
        record: Dict[str, Any] = {
            "action": action_type,
            "payload": payload,
            "timestamp": timestamp,
            "status": "success",
        }

        time.sleep(min(self.cooldown, 0.1))
        self.history.append(record)
        return True

    def get_recent_actions(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Retrieve the last N actions executed by this handler.

        Args:
            limit: Maximum number of recent actions to return.

        Returns:
            List of action history records.
        """
        return self.history[-limit:] if limit > 0 else []

    def clear_history(self) -> int:
        """Clear all recorded action history.

        Returns:
            Count of removed history items.
        """
        count: int = len(self.history)
        self.history.clear()
        return count
