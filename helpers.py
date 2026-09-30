import time
import logging
from typing import Union, Optional

logger = logging.getLogger(__name__)

def format_game_timestamp(seconds: float) -> str:
    """Convert raw float seconds into a human-readable duration string."""
    minutes, secs = divmod(int(seconds), 60)
    return f"{minutes:02d}m{secs:02d}s"

def get_retry_delay(attempt: int, base_delay: float = 1.0) -> float:
    """Calculate exponential backoff duration for network operations."""
    return base_delay * (2 ** (attempt - 1))

def validate_player_id(player_id: Union[int, str]) -> Optional[str]:
    """Sanitize and validate player identifiers for the gaming API."""
    try:
        clean_id = str(player_id).strip()
        if not clean_id:
            return None
        return clean_id
    except (ValueError, TypeError):
        return None

def log_performance_metrics(func_name: str, start_time: float) -> None:
    """Record the execution time of automation routines."""
    elapsed = time.perf_counter() - start_time
    logger.info(f"Routine '{func_name}' completed in {elapsed:.4f} seconds")