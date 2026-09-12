import re

def validate_game_input(user_input: str) -> bool:
    """
    Validates player input for gaming automation tasks.
    Ensures input is alphanumeric and within length constraints.
    """
    if not user_input or not isinstance(user_input, str):
        return False
    
    # Only allow alphanumeric characters, length 3-32
    pattern = r'^[a-zA-Z0-9]{3,32}$'
    return bool(re.match(pattern, user_input))

def sanitize_macro_command(command: str) -> str:
    """
    Basic sanitization to strip unsafe characters.
    """
    return re.sub(r'[^a-zA-Z0-9_]', '', command)

def validate_coordinate_range(x: int, y: int, max_x: int = 1920, max_y: int = 1080) -> bool:
    """
    Ensures screen coordinates are within defined game bounds.
    """
    return 0 <= x <= max_x and 0 <= y <= max_y