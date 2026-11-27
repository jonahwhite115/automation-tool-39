import logging

# Input validation for gaming automation inputs
def validate_game_input(data: dict) -> bool:
    """Validates player action data for range and type consistency."""
    required_fields = ['action_id', 'coordinates', 'intensity']
    
    try:
        # Check for presence of required gaming telemetry keys
        if not all(field in data for field in required_fields):
            logging.error(f"missing required telemetry fields: {data.keys()}")
            return False
        
        # Verify coordinates are valid pixel or world space integers
        x, y = data['coordinates']
        if not (isinstance(x, int) and isinstance(y, int)):
            return False
            
        # Verify intensity range for automation scripts (0.0 to 1.0)
        if not (0.0 <= data['intensity'] <= 1.0):
            return False
            
        return True
    except (KeyError, TypeError, ValueError) as e:
        logging.error(f"validation failure due to malformed data: {e}")
        return False

def sanitize_input(user_input: str) -> str:
    """Removes non-alphanumeric chars to prevent injection in gaming consoles."""
    return ''.join(c for c in user_input if c.isalnum())
