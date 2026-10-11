import time
from typing import Dict, List, Optional, Any, Callable


class GameEventHandler:
    """Manages and dispatches automated actions based on game state events."""

    def __init__(self, cooldown: float = 0.5) -> None:
        self.cooldown: float = cooldown
        self._handlers: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}
        self._last_trigger_times: Dict[str, float] = {}

    def register_listener(
        self, event_type: str, callback: Callable[[Dict[str, Any]], None]
    ) -> None:
        """Registers a callback function to be executed when a specific event occurs."""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(callback)

    def trigger_event(self, event_type: str, payload: Dict[str, Any]) -> bool:
        """Triggers event processing if the event cooldown period has passed."""
        current_time = time.time()
        last_time = self._last_trigger_times.get(event_type, 0.0)

        if current_time - last_time < self.cooldown:
            return False

        self._last_trigger_times[event_type] = current_time

        if event_type in self._handlers:
            for listener in self._handlers[event_type]:
                listener(payload)
            return True

        return False

    def clear_listeners(self, event_type: Optional[str] = None) -> None:
        """Clears listeners for a specific event type, or all event types if None."""
        if event_type is None:
            self._handlers.clear()
            self._last_trigger_times.clear()
        elif event_type in self._handlers:
            del self._handlers[event_type]
            self._last_trigger_times.pop(event_type, None)