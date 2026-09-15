import re

def validate_game_input(user_input: str) -> bool:
    """
    Validates player commands to prevent injection 
    and ensure valid action format.
    """
    # Pattern allows alphanumeric commands and basic dash separators
    pattern = r'^[a-zA-Z0-9_-]{1,20}$'
    return bool(re.match(pattern, user_input))

def validate_numeric_input(value: str, min_val: int, max_val: int) -> bool:
    """
    Ensures numerical configurations are within safe bounds 
    for gaming automation variables.
    """
    try:
        num = int(value)
        return min_val <= num <= max_val
    except ValueError:
        return False

def sanitize_input(data: str) -> str:
    """
    Strip whitespaces and cast to lowercase for safety.
    """
    return data.strip().lower()