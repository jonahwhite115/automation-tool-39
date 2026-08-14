import json
import os


def load_game_data(file_path):
    """Load game data from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON: {e}")


def save_game_data(file_path, data):
    """Save game data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_game_data(file_path, new_data):
    """Update existing game data with new data."""
    existing_data = load_game_data(file_path)
    existing_data.update(new_data)
    save_game_data(file_path, existing_data)


if __name__ == '__main__':
    sample_data = {'level': 1, 'score': 1500}
    save_game_data('game_data.json', sample_data)
    loaded_data = load_game_data('game_data.json')
    print(loaded_data)
    update_game_data('game_data.json', {'score': 2000})
    print(load_game_data('game_data.json'))