import time
from typing import Dict, List, Any, Callable

class GameEventProcessor:
    """Processes real-time game events and coordinates macro executions."""

    def __init__(self, cooldown_seconds: float = 0.1):
        self.cooldown_seconds = cooldown_seconds
        self.event_handlers: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}
        self.last_execution_time: float = 0.0

    def register_handler(self, event_type: str, handler: Callable[[Dict[str, Any]], None]) -> None:
        """Registers a callback handler for a specific game event type."""
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)

    def dispatch(self, event_type: str, data: Dict[str, Any]) -> bool:
        """Dispatches an event to all registered handlers if cooldown has expired."""
        current_time = time.time()
        if current_time - self.last_execution_time < self.cooldown_seconds:
            return False

        handlers = self.event_handlers.get(event_type, [])
        if not handlers:
            return False

        for handler in handlers:
            handler(data)

        self.last_execution_time = current_time
        return True

    def process_batch(self, events: List[Dict[str, Any]]) -> int:
        """Processes a list of queued game events sequentially."""
        processed_count = 0
        for event in events:
            event_type = event.get("type")
            event_data = event.get("data", {})
            if event_type and self.dispatch(event_type, event_data):
                processed_count += 1
        return processed_count
