import logging
from typing import Any, Optional

logger = logging.getLogger('automation-tool-39')

class AutomationError(Exception):
    """Base exception for automation-tool-39 operations."""
    pass

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """
    Executes a game-related helper function with comprehensive error handling.
    Returns the result if successful, None if an error occurs.
    """
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid input data for {func.__name__}: {e}")
    except ConnectionError as e:
        logger.error(f"Network failure during {func.__name__}: {e}")
    except Exception as e:
        logger.critical(f"Unexpected system failure in {func.__name__}: {e}")
    return None

def validate_game_state(state: Any) -> bool:
    """
    Ensures game state object is valid before processing.
    """
    if state is None:
        logger.warning("Empty game state received.")
        return False
    if not isinstance(state, dict):
        logger.error("Invalid game state format: dictionary expected.")
        return False
    return True