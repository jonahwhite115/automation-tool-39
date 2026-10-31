import time
from typing import Callable, List, Dict, Any, Optional

class MacroAction:
    """Represents an individual macro action with delay and execution logic."""
    def __init__(self, name: str, func: Callable[[], Any], cooldown: float = 0.1):
        self.name = name
        self.func = func
        self.cooldown = cooldown
        self.last_executed = 0.0

    def can_execute(self) -> bool:
        return (time.time() - self.last_executed) >= self.cooldown

    def execute(self) -> Any:
        if not self.can_execute():
            return None
        self.last_executed = time.time()
        return self.func()


class GameAutomationCore:
    """Core engine managing macro sequences and gaming automation loops."""
    def __init__(self, target_fps: int = 60):
        self.target_fps = target_fps
        self.frame_delay = 1.0 / target_fps
        self.action_queue: List[MacroAction] = []
        self.is_running = False

    def register_action(self, name: str, func: Callable[[], Any], cooldown: float = 0.1) -> None:
        """Register a new gaming automation macro action."""
        action = MacroAction(name, func, cooldown)
        self.action_queue.append(action)

    def process_frame(self) -> Dict[str, Any]:
        """Execute pending actions in the queue for the current frame."""
        results = {}
        for action in self.action_queue:
            if action.can_execute():
                results[action.name] = action.execute()
        return results

    def run_tick(self) -> Dict[str, Any]:
        """Run a single loop iteration with frame timing control."""
        start_time = time.time()
        results = self.process_frame()
        elapsed = time.time() - start_time
        sleep_time = self.frame_delay - elapsed
        if sleep_time > 0:
            time.sleep(sleep_time)
        return results
