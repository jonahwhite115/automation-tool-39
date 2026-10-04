import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Executes gaming automation tasks with safety wrappers."""
    try:
        return func(*args, **kwargs)
    except (ConnectionError, TimeoutError) as e:
        logger.error(f"Network failure in {func.__name__}: {e}")
    except ValueError as e:
        logger.error(f"Invalid configuration parameter: {e}")
    except Exception as e:
        logger.critical(f"Unexpected error in {func.__name__}: {type(e).__name__} - {e}")
    return None

def validate_game_state(state: dict) -> bool:
    """Checks integrity of retrieved game telemetry data."""
    try:
        if not isinstance(state, dict):
            return False
        required_keys = {'health', 'pos', 'active'}
        return all(key in state for key in required_keys)
    except Exception:
        return False

def format_telemetry(data: Optional[dict]) -> dict:
    """Sanitizes and formats raw telemetry packets."""
    default = {"health": 0, "pos": (0, 0), "active": False}
    if data is None or not isinstance(data, dict):
        return default
    return {**default, **data}