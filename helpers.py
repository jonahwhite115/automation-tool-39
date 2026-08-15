import random
import time
from typing import List


def random_choice(choices: List[str]) -> str:
    """Returns a random choice from a list."
    return random.choice(choices)


def wait_for(seconds: int) -> None:
    """Pauses the execution for a given number of seconds."
    time.sleep(seconds)


def find_highest_score(scores: List[int]) -> int:
    """Returns the highest score from a list of scores."
    return max(scores) if scores else 0


def load_game_data(file_path: str) -> dict:
    """Loads game data from a JSON file and returns it as a dictionary."
    import json
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path: str, data: dict) -> None:
    """Saves game data to a JSON file from a dictionary."""
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)