import time
from typing import List, Optional

def get_timestamp() -> float:
    """Returns the current high-precision system time."""
    return time.perf_counter()

def format_player_stats(player_name: str, scores: List[int]) -> str:
    """Formats a list of game scores into a display string."""
    avg_score = sum(scores) / len(scores) if scores else 0
    return f"Player {player_name}: Avg {avg_score:.2f} across {len(scores)} games"

def validate_game_session(session_id: Optional[str]) -> bool:
    """Checks if the provided game session identifier is valid.

    Args:
        session_id: The unique identifier string for the session.

    Returns:
        bool: True if the session ID is valid, False otherwise.
    """
    if not session_id or len(session_id) < 8:
        return False
    return session_id.isalnum()

def calculate_latency(start_time: float) -> float:
    """Calculates latency in milliseconds based on start time."""
    return (get_timestamp() - start_time) * 1000

def get_active_nodes(nodes: List[str], filter_key: str = "active") -> List[str]:
    """Filters list of game nodes based on a prefix key."""
    return [node for node in nodes if filter_key in node]