import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, backoff_factor=1):
    """
    Perform a network request with retry logic.
    
    :param url: URL to make the request to.
    :param max_retries: Maximum number of retries.
    :param backoff_factor: Backoff factor for wait time.
    :return: Response object if successful.
    """
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except RequestException as e:
            print(f"Request failed: {e}")
            retries += 1
            wait_time = backoff_factor * (2 ** (retries - 1))
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
    raise Exception(f"Failed to retrieve data from {url} after {max_retries} attempts")
