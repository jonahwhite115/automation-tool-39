import collections
import time
from typing import Dict, List, Tuple


class ActionFrame:
    # Utilize slots to minimize object instantiation overhead and memory footprint at high FPS
    __slots__ = ("action_id", "input_sequence", "priority", "timestamp")

    def __init__(
        self, action_id: str, input_sequence: List[str], priority: int
    ):
        self.action_id = action_id
        self.input_sequence = input_sequence
        self.priority = priority
        self.timestamp = time.perf_counter()


class GameAutomationEngine:
    """Core engine to process and dispatch macro actions with optimized execution queues."""

    def __init__(self, tick_rate_hz: int = 60):
        self.tick_rate_hz = tick_rate_hz
        self.tick_interval = 1.0 / tick_rate_hz
        # Use deque for fast O(1) pops and appends during high-frequency cycles
        self._action_queue: collections.deque[ActionFrame] = collections.deque()
        self._history_cache: Dict[str, float] = {}

    def queue_action(
        self, action_id: str, input_sequence: List[str], priority: int = 1
    ) -> None:
        """Queues a macro sequence, discarding old duplicates to prevent input flooding."""
        now = time.perf_counter()
        if (
            action_id in self._history_cache
            and now - self._history_cache[action_id] < 0.05
        ):
            return

        frame = ActionFrame(action_id, input_sequence, priority)
        # Prioritize high-priority inputs (e.g. panic heals) by placing them first
        if priority > 5:
            self._action_queue.appendleft(frame)
        else:
            self._action_queue.append(frame)

        self._history_cache[action_id] = now

    def process_next_batch(self) -> List[Tuple[str, List[str]]]:
        """Processes the queued inputs optimized for the targeted frame budget."""
        processed_actions = []
        start_time = time.perf_counter()

        # Strict timing constraint to prevent micro-stuttering in the game thread
        while self._action_queue:
            if time.perf_counter() - start_time > self.tick_interval:
                break

            frame = self._action_queue.popleft()
            processed_actions.append((frame.action_id, frame.input_sequence))

        # Performance maintenance: clear old memory entries periodically
        if len(self._history_cache) > 500:
            current_time = time.perf_counter()
            self._history_cache = {
                k: v
                for k, v in self._history_cache.items()
                if current_time - v < 5.0
            }

        return processed_actions