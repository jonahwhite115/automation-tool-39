import time
from typing import Dict, Any, List


class GameActionProcessor:
    """Processes and validates incoming game macro actions in the main loop."""

    ALLOWED_ACTIONS = {"attack", "cast_spell", "use_item", "move_to"}

    def __init__(self, actions_queue: List[Dict[str, Any]]):
        self.actions_queue = actions_queue
        self.processed_count = 0
        self.failed_count = 0

    def validate_action_payload(self, raw_action: Dict[str, Any]) -> bool:
        """Validates structure, command types, and parameters of an incoming action."""
        if not isinstance(raw_action, dict):
            return False

        action_type = raw_action.get("action")
        if not action_type or action_type not in self.ALLOWED_ACTIONS:
            return False

        delay = raw_action.get("delay", 0.0)
        if not isinstance(delay, (int, float)) or delay < 0.0 or delay > 10.0:
            return False

        if action_type in ("attack", "cast_spell"):
            target_id = raw_action.get("target_id")
            if not isinstance(target_id, int) or target_id <= 0:
                return False

        if action_type == "move_to":
            coords = raw_action.get("coordinates")
            if not isinstance(coords, (tuple, list)) or len(coords) != 2:
                return False
            if not all(isinstance(c, (int, float)) for c in coords):
                return False

        return True

    def run_loop(self) -> Dict[str, int]:
        """Main processing loop validating and executing incoming game actions."""
        for raw_action in self.actions_queue:
            if not self.validate_action_payload(raw_action):
                self.failed_count += 1
                continue

            self.execute_action(raw_action)
            self.processed_count += 1

        return {"processed": self.processed_count, "failed": self.failed_count}

    def execute_action(self, action: Dict[str, Any]) -> None:
        """Executes a verified game action payload."""
        delay = action.get("delay", 0.0)
        if delay > 0:
            time.sleep(min(delay, 0.01))
