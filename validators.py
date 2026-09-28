class ValidationError(Exception):
    """Custom exception for input validation failures in gaming automation."""
    pass

def validate_game_input(data: dict, required_keys: list):
    """Checks if input data contains all mandatory keys and valid types."""
    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required key: {key}")
    
    if not isinstance(data.get('action_delay'), (int, float)):
        raise ValidationError("Invalid action_delay: must be numeric")
    
    if data.get('action_delay', 0) < 0:
        raise ValidationError("Action delay cannot be negative")

def sanitize_input(user_input: str) -> str:
    """Removes non-alphanumeric characters to prevent injection issues."""
    return ''.join(char for char in user_input if char.isalnum())

def validate_coordinate_range(x: int, y: int, bounds: tuple):
    """Ensures screen coordinates remain within game window bounds."""
    width, height = bounds
    if not (0 <= x <= width and 0 <= y <= height):
        raise ValidationError(f"Coordinates ({x}, {y}) outside screen bounds")