import random
import time
from typing import Tuple


def calculate_click_position(rect: Tuple[int, int, int, int], padding: int = 5) -> Tuple[int, int]:
    """Calculate a random click coordinate inside a bounding rectangle with padding."""
    x, y, width, height = rect
    inner_x1 = x + padding
    inner_y1 = y + padding
    inner_x2 = x + width - padding
    inner_y2 = y + height - padding

    if inner_x1 >= inner_x2 or inner_y1 >= inner_y2:
        return (x + width // 2, y + height // 2)

    click_x = random.randint(inner_x1, inner_x2)
    click_y = random.randint(inner_y1, inner_y2)
    return (click_x, click_y)


def human_delay(min_seconds: float = 0.1, max_seconds: float = 0.35) -> None:
    """Introduce a randomized delay to simulate natural human input timing."""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)


def format_game_timestamp(seconds: float) -> str:
    """Format total elapsed seconds into a standard MM:SS string."""
    minutes = int(seconds // 60)
    remaining_seconds = int(seconds % 60)
    return f"{minutes:02d}:{remaining_seconds:02d}"