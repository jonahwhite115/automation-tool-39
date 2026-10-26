import re

# Input validation for gaming automation parameters
def validate_game_config(config_data: dict) -> bool:
    """
    Ensures user provided configurations meet criteria
    for automated game actions.
    """
    required_keys = ['macro_name', 'interval', 'key_bind']
    
    # Check for missing keys
    if not all(key in config_data for key in required_keys):
        return False

    # Validate interval is a positive float
    try:
        interval = float(config_data['interval'])
        if interval <= 0:
            return False
    except (ValueError, TypeError):
        return False

    # Validate key_bind matches standard input format (single alphanumeric)
    if not re.match(r'^[a-zA-Z0-9]$', str(config_data['key_bind'])):
        return False

    return True

def validate_user_input(value: str, min_len: int = 1) -> bool:
    """
    Basic string validation to prevent injection or empty strings
    """
    if not value or not isinstance(value, str):
        return False
    
    # Remove dangerous shell characters
    clean_value = re.sub(r'[^a-zA-Z0-9_\-\s]', '', value)
    return len(clean_value) >= min_len