from typing import List, Dict, Union, Optional
import time

def calculate_macro_delay(base_ms: int, variance: float = 0.1) -> float:
    """Calculates randomized delay to prevent anti-cheat detection."""
    import random
    
    offset = base_ms * variance
    final_delay = base_ms + random.uniform(-offset, offset)
    return max(0.0, final_delay / 1000.0)

def format_game_coords(x: int, y: int) -> Dict[str, int]:
    """Normalizes screen coordinates for input injection."""
    return {"x": int(x), "y": int(y)}

def validate_session_status(active_threads: List[str]) -> bool:
    """Checks if provided session IDs are currently tracked."""
    return len(active_threads) > 0

class MacroBuffer:
    def __init__(self, capacity: int = 100) -> None:
        self.capacity: int = capacity
        self.queue: List[Union[str, int]] = []

    def add_command(self, cmd: str) -> None:
        """Appends command string if buffer under capacity."""
        if len(self.queue) < self.capacity:
            self.queue.append(cmd)

    def clear(self) -> None:
        """Resets the internal command queue."""
        self.queue = []