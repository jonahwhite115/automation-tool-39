import time
from typing import Dict, Any, List, Optional
from logger import setup_logger

logger = setup_logger("processor")


class ActionProcessor:
    """Processes and dispatches gaming macro actions cleanly."""

    def __init__(self, execution_delay: float = 0.05) -> None:
        self.execution_delay = execution_delay
        self._action_queue: List[Dict[str, Any]] = []

    def queue_action(self, action_type: str, payload: Dict[str, Any]) -> None:
        """Enqueue a new action for execution."""
        event = {"type": action_type, "data": payload, "timestamp": time.time()}
        self._action_queue.append(event)
        logger.debug(f"Action queued: {action_type}")

    def clear_queue(self) -> int:
        """Purge pending actions from the queue."""
        count = len(self._action_queue)
        self._action_queue.clear()
        logger.info(f"Cleared {count} pending actions")
        return count

    def process_next(self) -> Optional[Dict[str, Any]]:
        """Process the next action in the queue."""
        if not self._action_queue:
            return None

        action = self._action_queue.pop(0)
        action_type = action.get("type")
        payload = action.get("data", {})

        if action_type == "key_press":
            key = payload.get("key", "unknown")
            logger.info(f"Simulating key press: {key}")
        elif action_type == "mouse_click":
            x, y = payload.get("x", 0), payload.get("y", 0)
            logger.info(f"Simulating mouse click at ({x}, {y})")
        else:
            logger.warning(f"Unknown action type: {action_type}")

        time.sleep(self.execution_delay)
        return action
