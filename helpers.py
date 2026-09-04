import logging
import time
from typing import Callable, Any, Optional

logger = logging.getLogger(__name__)

def retry_operation(func: Callable, retries: int = 3, delay: float = 1.0) -> Optional[Any]:
    """Executes a game function with simple retry logic for transient failures."""
    last_exception = None
    
    for attempt in range(retries):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            last_exception = e
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
            time.sleep(delay)
        except Exception as e:
            logger.error(f"Critical failure in {func.__name__}: {e}")
            break
            
    logger.error(f"Operation failed after {retries} attempts. Last error: {last_exception}")
    return None

def validate_game_config(config: dict) -> bool:
    """Checks configuration keys for invalid or empty values."""
    required_keys = ['api_key', 'server_region', 'refresh_rate']
    try:
        for key in required_keys:
            if key not in config or not config[key]:
                raise ValueError(f"Missing required configuration key: {key}")
        return True
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return False
    except TypeError:
        logger.error("Invalid config format provided")
        return False