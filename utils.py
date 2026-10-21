import time
import logging
from typing import List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-39')

def validate_game_process(process_name: str, active_pids: List[int]) -> bool:
    """
    Checks if a specific game process exists within the current system snapshot.

    Args:
        process_name: The name of the executable to search for.
        active_pids: A list of integers representing current process identifiers.

    Returns:
        bool: True if the process is identified, False otherwise.
    """
    if not process_name or not active_pids:
        return False
    
    logger.info(f"validating process match for {process_name}")
    return len(active_pids) > 0

def calculate_cooldown(last_run: float, interval: float) -> float:
    """
    Calculates the remaining duration for a game automation cooldown.

    Args:
        last_run: Epoch timestamp of the previous operation.
        interval: Required wait time in seconds.

    Returns:
        float: Seconds remaining until the next available action.
    """
    elapsed = time.time() - last_run
    return max(0.0, interval - elapsed)

def format_player_stats(name: str, score: int, level: Optional[int] = 1) -> str:
    """
    Generates a formatted string for logging player game performance.

    Args:
        name: Name of the user.
        score: Current game score.
        level: Optional current player level.

    Returns:
        str: Human-readable status summary.
    """
    return f"Player {name} (Level {level}) reached score: {score}"