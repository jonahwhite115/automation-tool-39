import logging

logger = logging.getLogger(__name__)

def validate_game_input(data: dict) -> bool:
    """Validates input payload for automation tasks."""
    required_fields = ['action', 'delay', 'coordinates']
    
    # Verify presence of mandatory keys
    for field in required_fields:
        if field not in data:
            logger.error(f"Missing field: {field}")
            return False

    # Validate data types and constraints
    if not isinstance(data['action'], str):
        return False
    
    if not isinstance(data['delay'], (int, float)) or data['delay'] < 0:
        logger.warning("Invalid delay value provided")
        return False
        
    coords = data['coordinates']
    if not (isinstance(coords, list) and len(coords) == 2):
        logger.error("Coordinates must be a list of two values")
        return False
        
    if not all(isinstance(c, int) for c in coords):
        return False

    return True

def sanitize_input(value: str) -> str:
    """Cleans strings to prevent injection or errors."""
    return str(value).strip().lower()