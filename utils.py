import time
from typing import List, Optional

def get_timestamp() -> float:
    """Returns the current high-precision system time."""
    return time.time()

def format_player_name(name: str, prefix: Optional[str] = None) -> str:
    """Sanitizes and prefixes a player name for game logs."""
    clean_name = name.strip().lower().replace(" ", "_")
    if prefix:
        return f"{prefix}_{clean_name}"
    return clean_name

def validate_fps_limit(limit: int) -> bool:
    """Validates that the provided FPS limit is within safe hardware ranges."""
    return 30 <= limit <= 360

def batch_process_ids(ids: List[int], batch_size: int = 10) -> List[List[int]]:
    """Splits a large list of game object IDs into smaller chunks for processing."""
    return [ids[i : i + batch_size] for i in range(0, len(ids), batch_size)]

def calculate_cooldown_progress(elapsed: float, total: float) -> float:
    """Calculates the percentage of completion for a game skill cooldown."""
    if total <= 0:
        return 1.0
    progress = elapsed / total
    return min(max(progress, 0.0), 1.0)