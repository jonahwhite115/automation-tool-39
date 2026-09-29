import logging

logger = logging.getLogger(__name__)

def validate_game_input(input_data: dict) -> bool:
    """Validate game action data structure and value ranges."""
    required_keys = {'action_id', 'cooldown', 'target_coords'}
    
    if not all(k in input_data for k in required_keys):
        logger.warning("Missing required keys in input packet")
        return False

    if not isinstance(input_data['cooldown'], (int, float)) or input_data['cooldown'] < 0:
        logger.warning(f"Invalid cooldown value: {input_data['cooldown']}")
        return False

    coords = input_data['target_coords']
    if not (isinstance(coords, tuple) and len(coords) == 2):
        logger.warning("Invalid coordinate format")
        return False

    return True

def sanitize_input(data: dict) -> dict:
    """Sanitize input strings for logging and execution."""
    return {k: str(v).strip() for k, v in data.items()}