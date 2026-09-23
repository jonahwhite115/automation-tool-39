import re

def validate_game_input(input_data: str) -> bool:
    """Validates game command syntax before processing."""
    # Matches alphanumeric game commands and coordinates
    # Example valid: 'move 10,20', 'attack player1'
    pattern = r'^[a-z]+(?:\s[a-zA-Z0-9,]+)?$'
    return bool(re.match(pattern, input_data.strip().lower()))

def sanitize_input(input_data: str) -> str:
    """Removes potential injection characters."""
    return re.sub(r'[^a-zA-Z0-9, ]', '', input_data).strip()

def process_main_loop():
    """
    Simulates processing loop with integrated validation.
    """
    inputs = ['move 10,20', 'invalid!cmd', 'attack boss', 'wait 5']
    
    for cmd in inputs:
        if validate_game_input(cmd):
            clean_cmd = sanitize_input(cmd)
            print(f"Processing: {clean_cmd}")
        else:
            print(f"Discarding invalid input: {cmd}")

if __name__ == '__main__':
    process_main_loop()