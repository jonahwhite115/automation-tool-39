import logging

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for game automation input failures."""
    pass

def validate_game_coords(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Ensures coordinates are within game window bounds."""
    try:
        if not (0 <= x < screen_width and 0 <= y < screen_height):
            raise ValidationError(f"Coordinates ({x}, {y}) outside bounds {screen_width}x{screen_height}")
        return True
    except TypeError as e:
        logger.error(f"Invalid coordinate type provided: {e}")
        return False
    except ValidationError as e:
        logger.warning(f"Validation failed: {e}")
        return False

def sanitize_input(value: str, max_length: int = 50) -> str:
    """Sanitizes user input strings to prevent injection or errors."""
    if not isinstance(value, str):
        return ""
    
    # Truncate and strip whitespace for safety
    clean_value = value.strip()[:max_length]
    
    if not clean_value:
        logger.debug("Sanitized input resulted in empty string")
        
    return clean_value