import logging

# Input validation for gaming automation inputs
def validate_game_input(data: dict) -> bool:
    """Validates player action data for processing integrity."""
    required_keys = ['action_id', 'coordinate_x', 'coordinate_y', 'timestamp']
    
    try:
        # Verify presence of all required fields
        if not all(k in data for k in required_keys):
            logging.error("Missing required keys in input packet")
            return False
            
        # Range validation for game screen coordinates
        if not (0 <= data['coordinate_x'] <= 1920 and 0 <= data['coordinate_y'] <= 1080):
            logging.warning("Coordinate out of screen bounds: %s", data)
            return False
            
        # Action type safety check
        if not isinstance(data['action_id'], int) or data['action_id'] < 0:
            logging.error("Invalid action_id format")
            return False
            
        return True
    except (TypeError, ValueError) as e:
        logging.error("Validation processing error: %s", e)
        return False

def sanitize_input_payload(data: dict) -> dict:
    """Cleans dictionary values for safe execution."""
    return {
        'action_id': int(data.get('action_id', 0)),
        'coordinate_x': float(data.get('coordinate_x', 0.0)),
        'coordinate_y': float(data.get('coordinate_y', 0.0)),
        'timestamp': str(data.get('timestamp', '0'))
    }