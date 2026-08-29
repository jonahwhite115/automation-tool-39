import re
def validate_player_name(name):
    """Validate player name for gaming automation."""
    if not isinstance(name, str):
        return False
    if len(name) < 3 or len(name) > 20:
        return False
    if not re.match(r'^[a-zA-Z0-9_]+$', name):
        return False
    return True

def validate_action(action):
    """Check if action is valid in the game."""
    valid_actions = ['move', 'attack', 'defend', 'use_item', 'collect']
    return isinstance(action, str) and action in valid_actions

def validate_coordinates(x, y):
    """Validate screen coordinates for game actions."""
    if not isinstance(x, int) or not isinstance(y, int):
        return False
    if x < 0 or x > 1920 or y < 0 or y > 1080:
        return False
    return True

def validate_input(data):
    """Main validation function for input data."""
    if not isinstance(data, dict):
        return False, "Input must be a dictionary"
    if 'player' not in data or not validate_player_name(data['player']):
        return False, "Invalid player name"
    if 'action' not in data or not validate_action(data['action']):
        return False, "Invalid action"
    if data['action'] == 'move':
        if 'x' not in data or 'y' not in data or not validate_coordinates(data['x'], data['y']):
            return False, "Invalid move coordinates"
    return True, None

def main_processing_loop(input_list):
    """Main loop that processes and validates game inputs."""
    results = []
    for data in input_list:
        is_valid, error = validate_input(data)
        if is_valid:
            # Process the valid input
            action = data['action']
            player = data['player']
            if action == 'move':
                print(f"Automating move for {player} to ({data['x']}, {data['y']})")
            else:
                print(f"Automating {action} for {player}")
            results.append({"status": "processed", "input": data})
        else:
            print(f"Validation failed: {error} for {data}")
            results.append({"status": "invalid", "input": data, "error": error})
    return results

if __name__ == "__main__":
    test_inputs = [
        {"player": "PlayerOne", "action": "move", "x": 500, "y": 300},
        {"player": "Bad@Name", "action": "attack"},
        {"player": "Gamer99", "action": "defend"},
        {"player": "Hero", "action": "move", "x": 2000, "y": 100}
    ]
    processed = main_processing_loop(test_inputs)
    print("Results:", processed)
