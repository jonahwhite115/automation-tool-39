import time
from typing import Dict, List, Optional, Any, Callable


class ActionEngine:
    """Manages and executes automated macro sequences for gaming tasks."""

    def __init__(self, default_delay: float = 0.5) -> None:
        """Initialize the ActionEngine with a default inter-action delay.

        Args:
            default_delay: Time in seconds to wait between action executions.
        """
        self.default_delay: float = default_delay
        self.queue: List[Dict[str, Any]] = []
        self.active: bool = False

    def register_action(
        self,
        name: str,
        callback: Callable[..., bool],
        params: Optional[Dict[str, Any]] = None,
        delay: Optional[float] = None,
    ) -> None:
        """Register a gaming macro action into the execution queue.

        Args:
            name: Human-readable identifier for the action.
            callback: Executable function returning success status.
            params: Dictionary of kwargs passed to the callback.
            delay: Custom delay in seconds after executing this specific action.
        """
        action_item: Dict[str, Any] = {
            "name": name,
            "callback": callback,
            "params": params or {},
            "delay": delay if delay is not None else self.default_delay,
        }
        self.queue.append(action_item)

    def execute_sequence(self, max_retries: int = 3) -> Dict[str, bool]:
        """Execute all queued actions in order, with automatic retry logic.

        Args:
            max_retries: Maximum attempts per failed action.

        Returns:
            Dictionary mapping action names to their final completion status.
        """
        self.active = True
        results: Dict[str, bool] = {}

        for item in self.queue:
            if not self.active:
                break

            action_name: str = item["name"]
            func: Callable[..., bool] = item["callback"]
            kwargs: Dict[str, Any] = item["params"]
            delay: float = item["delay"]

            success: bool = False
            for attempt in range(1, max_retries + 1):
                try:
                    success = func(**kwargs)
                    if success:
                        break
                except Exception:
                    success = False
                time.sleep(0.1 * attempt)

            results[action_name] = success
            time.sleep(delay)

        self.active = False
        return results

    def clear_queue(self) -> int:
        """Clear all pending actions from the queue.

        Returns:
            Number of actions removed from the queue.
        """
        count: int = len(self.queue)
        self.queue.clear()
        return count
