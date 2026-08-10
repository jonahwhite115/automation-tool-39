import time
import requests
from requests.exceptions import RequestException


def retry_request(url, max_retries=3, delay=2):
    """
    Perform a GET request with retry logic.
    
    :param url: The URL to request.
    :param max_retries: The maximum number of retries.
    :param delay: The delay between retries in seconds.
    :return: The response object if successful, None otherwise.
    """
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except RequestException as e:
            attempt += 1
            print(f'Attempt {attempt} failed: {e}')
            if attempt < max_retries:
                print(f'Retrying in {delay} seconds...')
                time.sleep(delay)
            else:
                print('All attempts failed.')
    return None
