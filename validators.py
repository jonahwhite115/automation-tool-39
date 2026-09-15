import logging

# Configure logger for automation-tool-39
logger = logging.getLogger('automation-tool-39')

def validate_game_input(data):
    """
    Validates game action dictionary structure and value types.
    Ensures input is safe for processing loop execution.
    """
    required_keys = {'action', 'payload', 'timestamp'}
    
    # Validate dictionary structure
    if not isinstance(data, dict) or not required_keys.issubset(data.keys()):
        logger.error(f"Invalid input structure: {data}")
        return False

    # Validate action type constraints
    if not isinstance(data['action'], str) or len(data['action']) > 32:
        logger.warning(f"Action string malformed: {data['action']}")
        return False

    # Validate payload type (must be dictionary)
    if not isinstance(data['payload'], dict):
        logger.warning("Payload must be a dictionary")
        return False

    # Validate numeric bounds for simulation
    if 'intensity' in data['payload']:
        val = data['payload']['intensity']
        if not isinstance(val, (int, float)) or not (0 <= val <= 100):
            logger.error("Intensity outside valid range 0-100")
            return False
            
    return True

def sanitize_input(data):
    """
    Cleans input payload of unexpected keys before processing.
    """
    allowed_keys = {'intensity', 'target', 'mode'}
    return {k: v for k, v in data.items() if k in allowed_keys}