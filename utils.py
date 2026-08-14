import time
import requests
from typing import Callable

def retry_on_failure(max_retries: int, delay: float) -> Callable:
    """Decorator to implement retry logic on network operations."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as e:
                    attempts += 1
                    if attempts < max_retries:
                        print(f'Retry {attempts}/{max_retries} in {delay}s...')
                        time.sleep(delay)
                    else:
                        print('Max retries reached. Raising exception.')
                        raise e
        return wrapper
    return decorator

@retry_on_failure(max_retries=3, delay=2)
def fetch_data(url: str) -> dict:
    """Fetch data from the given URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses
    return response.json()  # Return the JSON content
