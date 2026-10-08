from typing import List, Optional, Dict, Any
import time

def calculate_cooldown(last_action_time: float, interval: float) -> float:
    """Calculates remaining time until next permitted action."""
    elapsed = time.time() - last_action_time
    return max(0.0, interval - elapsed)

def format_player_stats(stats: Dict[str, Any], username: str) -> str:
    """Converts raw stats dictionary into a readable status string."""
    level = stats.get('level', 1)
    xp = stats.get('xp', 0)
    return f"[{username}] Level: {level} | XP: {xp}"

def filter_valid_targets(targets: List[Dict[str, Any]], min_level: int) -> List[Dict[str, Any]]:
    """Filters list of gaming targets based on level requirements."""
    return [t for t in targets if t.get('level', 0) >= min_level]

def generate_retry_delay(attempt: int, base_delay: float = 1.0) -> float:
    """Calculates exponential backoff delay for network requests."""
    return base_delay * (2 ** (attempt - 1))

def get_session_duration(start_time: float) -> str:
    """Formats elapsed session time into HH:MM:SS string."""
    seconds = int(time.time() - start_time)
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"