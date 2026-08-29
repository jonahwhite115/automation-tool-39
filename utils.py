import time
import random
import json
from typing import Tuple, Optional, Dict, Any

def get_random_delay(min_seconds: float, max_seconds: float) -> float:
    """Return a random delay between min and max seconds."""
    return random.uniform(min_seconds, max_seconds)

def wait_with_jitter(min_sec: float, max_sec: float) -> None:
    """Sleep for a random time within range to avoid detection."""
    delay = get_random_delay(min_sec, max_sec)
    time.sleep(delay)

def parse_game_coordinates(data: str) -> Optional[Tuple[int, int]]:
    """Parse 'x,y' string into coordinate tuple."""
    try:
        parts = data.strip().split(',')
        if len(parts) != 2:
            return None
        x = int(parts[0])
        y = int(parts[1])
        return (x, y)
    except (ValueError, AttributeError):
        return None

def load_game_config(filepath: str) -> Dict[str, Any]:
    """Load JSON config file for game settings."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        return {}

def calculate_distance(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
    """Calculate straight-line distance between two points."""
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    return (dx * dx + dy * dy) ** 0.5

def normalize_position(x: int, y: int, screen_width: int, screen_height: int) -> Tuple[float, float]:
    """Convert pixel coords to normalized 0-1 values."""
    if screen_width <= 0 or screen_height <= 0:
        return (0.0, 0.0)
    norm_x = x / screen_width
    norm_y = y / screen_height
    return (norm_x, norm_y)

def get_random_position_in_area(x: int, y: int, width: int, height: int) -> Tuple[int, int]:
    """Return random integer position inside the given area."""
    rx = x + random.randint(0, max(0, width))
    ry = y + random.randint(0, max(0, height))
    return (rx, ry)

class GameUtils:
    """Utility class for common gaming automation tasks."""
    def __init__(self, screen_size: Tuple[int, int]):
        self.screen_width = screen_size[0]
        self.screen_height = screen_size[1]

    def get_center(self) -> Tuple[int, int]:
        """Return center coordinates of the screen."""
        cx = self.screen_width // 2
        cy = self.screen_height // 2
        return (cx, cy)

    def is_within_bounds(self, x: int, y: int) -> bool:
        """Check if position is inside screen boundaries."""
        return (0 <= x < self.screen_width and 0 <= y < self.screen_height)

    def get_random_screen_position(self) -> Tuple[int, int]:
        """Generate random position anywhere on screen."""
        rx = random.randint(0, self.screen_width - 1)
        ry = random.randint(0, self.screen_height - 1)
        return (rx, ry)
