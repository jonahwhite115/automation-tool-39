import time
import requests


def retry_request(url, max_retries=3, wait_time=2):
    """Performs a GET request with retry logic."""
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except requests.exceptions.RequestException as err:
            print(f'Error occurred: {err}')
        retries += 1
        time.sleep(wait_time)  # Wait before retrying
    raise Exception('Max retries exceeded')


# Example of usage:
# data = retry_request('https://api.example.com/data')
# print(data)
