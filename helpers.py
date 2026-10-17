import random
import time
from typing import Tuple, Dict, Any


def human_delay(min_seconds: float = 0.5, max_seconds: float = 1.5) -> None:
    """Simulate human reaction time with a randomized delay."""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)


def calculate_xp_required(current_level: int, base_xp: int = 100, growth_factor: float = 1.5) -> int:
    """Calculate total XP required for the specified level."""
    if current_level < 1:
        return 0
    return int(base_xp * (current_level ** growth_factor))


def calculate_center_point(region: Tuple[int, int, int, int]) -> Tuple[int, int]:
    """
    Calculate the center coordinate (X, Y) from a region box (left, top, width, height).
    """
    left, top, width, height = region
    center_x = left + (width // 2)
    center_y = top + (height // 2)
    return center_x, center_y


def format_cooldown(seconds_remaining: float) -> str:
    """Format remaining seconds into readable MM:SS format."""
    if seconds_remaining <= 0:
        return "Ready"
    minutes = int(seconds_remaining) // 60
    seconds = int(seconds_remaining) % 60
    return f"{minutes:02d}:{seconds:02d}"


def parse_game_state(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize raw incoming telemetry data from game client."""
    max_hp = float(raw_data.get("max_hp", 1)) or 1.0
    current_hp = float(raw_data.get("hp", 0))
    return {
        "player_id": raw_data.get("pid", 0),
        "health_pct": round((current_hp / max_hp) * 100, 1),
        "is_in_combat": bool(raw_data.get("combat_flag", False)),
        "position": (raw_data.get("x", 0), raw_data.get("y", 0), raw_data.get("z", 0)),
    }
