import time
import logging
from typing import Any, Callable, Optional

logger = logging.getLogger('automation-tool-39')

def retry_operation(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Retry logic for unstable game server requests."""
    last_exception = None
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    raise last_exception

def format_game_coords(x: float, y: float, z: float) -> str:
    """Standardized coordinate string formatting for game engine."""
    return f"[{x:.2f}, {y:.2f}, {z:.2f}]"

def get_input_validation(value: Any, min_val: float, max_val: float) -> float:
    """Clamp numeric inputs to valid game ranges."""
    return float(max(min_val, min(value, max_val)))

def throttle_execution(interval: float):
    """Decorator for rate limiting game actions."""
    def decorator(func: Callable):
        last_called = [0.0]
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < interval:
                time.sleep(interval - elapsed)
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator