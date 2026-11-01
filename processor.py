import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field


@dataclass
class GameAction:
    action_type: str
    target_x: int
    target_y: int
    delay_after: float = 0.05
    payload: Dict[str, Any] = field(default_factory=dict)


class ActionProcessor:
    """Processes queued game automation actions with execution safety."""

    def __init__(self, execution_interval: float = 0.1):
        self.execution_interval = execution_interval
        self._queue: List[GameAction] = []
        self._last_execution: float = 0.0
        self._is_active: bool = True

    def enqueue(self, action: GameAction) -> None:
        """Add a single action to the processing queue."""
        if self._is_active:
            self._queue.append(action)

    def enqueue_batch(self, actions: List[GameAction]) -> None:
        """Add multiple actions to the processing queue at once."""
        for action in actions:
            self.enqueue(action)

    def process_next(self) -> Optional[GameAction]:
        """Process and execute the next action in the queue if ready."""
        if not self._queue:
            return None

        now = time.time()
        if now - self._last_execution < self.execution_interval:
            return None

        action = self._queue.pop(0)
        self._execute_action(action)
        self._last_execution = time.time()
        return action

    def _execute_action(self, action: GameAction) -> None:
        """Internal handler to dispatch game automation actions."""
        if action.action_type == "click":
            time.sleep(action.delay_after)
        elif action.action_type == "keypress":
            time.sleep(action.delay_after)

    def clear(self) -> None:
        """Purge all remaining actions in the queue."""
        self._queue.clear()

    def count(self) -> int:
        """Return remaining actions count."""
        return len(self._queue)
