import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Executes gaming-related automation tasks with boundary checks."""
    try:
        return func(*args, **kwargs)
    except TypeError as e:
        logger.error(f"Invalid argument type provided: {e}")
    except ValueError as e:
        logger.error(f"Value out of expected gaming range: {e}")
    except Exception as e:
        logger.critical(f"Unexpected automation runtime failure: {e}")
    return None

def validate_coordinates(x: int, y: int, bounds: tuple) -> bool:
    """Ensures mouse click coordinates fall within window frame."""
    width, height = bounds
    if not (0 <= x < width and 0 <= y < height):
        logger.warning(f"Coordinate ({x}, {y}) is outside valid screen bounds")
        return False
    return True

def retry_connection(func: callable, retries: int = 3) -> Optional[Any]:
    """Re-attempts network operations for unstable game APIs."""
    last_exception = None
    for attempt in range(retries):
        try:
            return func()
        except ConnectionError as e:
            last_exception = e
            logger.info(f"Connection attempt {attempt + 1} failed. Retrying...")
    logger.error(f"Failed after {retries} retries: {last_exception}")
    return None