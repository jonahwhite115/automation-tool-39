import time
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

def format_game_data(raw_data: Dict[str, Any], session_id: str) -> Dict[str, Any]:
    """
    Normalizes raw game data into a structured format for storage.

    Args:
        raw_data: The incoming dictionary from the game API.
        session_id: Unique identifier for the current gaming session.

    Returns:
        A cleaned dictionary containing formatted player stats.
    """
    return {
        "session_id": session_id,
        "timestamp": time.time(),
        "score": int(raw_data.get("points", 0)),
        "active": bool(raw_data.get("is_online", False))
    }

def validate_connection(latency: float, threshold: float = 100.0) -> bool:
    """
    Checks if the latency is within the acceptable gaming threshold.

    Args:
        latency: Current network latency in milliseconds.
        threshold: Maximum allowed latency in milliseconds.

    Returns:
        True if connection is stable, False otherwise.
    """
    if latency > threshold:
        logger.warning(f"High latency detected: {latency}ms")
        return False
    return True

def retry_operation(func: Any, retries: int = 3) -> Optional[Any]:
    """
    Attempts a function call multiple times before giving up.

    Args:
        func: Callable to execute.
        retries: Number of attempts to make.

    Returns:
        The result of the function call or None.
    """
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            logger.error(f"Attempt {i+1} failed: {e}")
            time.sleep(1)
    return None