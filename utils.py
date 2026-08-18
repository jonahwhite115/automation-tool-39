import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, delay=2):
    """
    Makes a network request to the given URL with retry logic.
    Retries the request up to max_retries times with a delay between attempts.
    """
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise error for bad responses
            return response.json()  # Assuming the response is JSON
        except RequestException as e:
            attempts += 1  
            print(f"Attempt {attempts} failed: {e}")
            if attempts < max_retries:
                time.sleep(delay)  # Wait before the next attempt
            else:
                print("Max retries reached.")
                return None  # Return None or raise an exception based on your needs

# Example usage:
#if __name__ == '__main__':
#    data = retry_request('https://api.example.com/data')
#    print(data)  # Handling data according to your needs