import time
import json
from functools import lru_cache

@lru_cache(maxsize=None)
def get_game_settings(game_id):
    """Fetch game settings from a configuration file."""
    with open(f'config/{game_id}_settings.json', 'r') as file:
        return json.load(file)

def calculate_optimal_frame_rate(target_fps):
    """Calculate the optimal frame rate based on target FPS."""
    return max(30, min(target_fps, 60))

def time_execution(func):
    """Decorator to time the execution of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'Execution time for {func.__name__}: {end_time - start_time:.4f} seconds')
        return result
    return wrapper

@time_execution
def run_game_logic(game_id):
    """Run main game logic for a specified game ID."""
    settings = get_game_settings(game_id)
    # Simulate game logic processing...
    time.sleep(0.1)  # Placeholder for game loop processing
    print(f'Game logic executed for {game_id} with settings: {settings}')