import random
import time
from typing import Tuple


def calculate_health_percentage(current_hp: int, max_hp: int) -> float:
    """Calculate current health as a percentage between 0.0 and 100.0."""
    if max_hp <= 0:
        return 0.0
    bounded_hp = max(0, min(current_hp, max_hp))
    return round((bounded_hp / max_hp) * 100.0, 2)


def get_randomized_delay(base_seconds: float, variance: float = 0.15) -> float:
    """Generate a randomized delay to simulate human-like interaction timing."""
    min_delay = max(0.01, base_seconds * (1.0 - variance))
    max_delay = base_seconds * (1.0 + variance)
    return round(random.uniform(min_delay, max_delay), 3)


def sleep_humanized(base_seconds: float, variance: float = 0.15) -> None:
    """Pause execution for a randomized duration to evade basic bot detection."""
    delay = get_randomized_delay(base_seconds, variance)
    time.sleep(delay)


def is_target_in_range(
    player_pos: Tuple[int, int], target_pos: Tuple[int, int], max_distance: float
) -> bool:
    """Check if a target position is within combat/interaction range."""
    dx = player_pos[0] - target_pos[0]
    dy = player_pos[1] - target_pos[1]
    distance_squared = dx * dx + dy * dy
    return distance_squared <= (max_distance * max_distance)


def format_cooldown(seconds_remaining: float) -> str:
    """Format remaining cooldown time into readable format (e.g. '01:23')."""
    total_seconds = max(0, int(seconds_remaining))
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"
