class ValidationError(Exception):
    """Custom exception for input validation failures in gaming automation."""
    pass

def validate_game_input(user_input: dict) -> bool:
    """Ensures input data contains required fields and valid data types."""
    required_keys = ['action_id', 'intensity', 'duration']
    
    # Check for missing keys
    for key in required_keys:
        if key not in user_input:
            raise ValidationError(f"missing required input field: {key}")

    # Validate data types and ranges
    if not isinstance(user_input['action_id'], int):
        raise ValidationError("action_id must be an integer")
        
    if not (0 <= user_input['intensity'] <= 100):
        raise ValidationError("intensity must be between 0 and 100")
        
    if not isinstance(user_input['duration'], (int, float)) or user_input['duration'] < 0:
        raise ValidationError("duration must be a non-negative number")

    return True

def sanitize_payload(payload: dict) -> dict:
    """Strips whitespace from string inputs before processing."""
    return {k: v.strip() if isinstance(v, str) else v for k, v in payload.items()}