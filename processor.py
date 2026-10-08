import time
import random
from typing import Callable, Any, Optional

def execute_with_retry(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """
    Executes a function with exponential backoff for network-related tasks.
    Suitable for intermittent gaming API connectivity issues.
    """
    last_exception = None
    
    for attempt in range(retries):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            last_exception = e
            wait_time = delay * (2 ** attempt) + random.uniform(0, 0.1)
            time.sleep(wait_time)
            continue
    
    raise last_exception or Exception("network operation failed after retries")

def fetch_game_data(api_client: Any, endpoint: str) -> dict:
    """
    Wrapper for fetching game data using retry logic.
    """
    def request_call():
        return api_client.get(endpoint)
    
    return execute_with_retry(request_call)
