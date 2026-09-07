import logging

logger = logging.getLogger(__name__)

def validate_game_input(user_input: str) -> bool:
    """Validates player commands for the automation tool."""
    if not user_input or not isinstance(user_input, str):
        logger.error("invalid input type received")
        return False
    
    clean_input = user_input.strip().lower()
    allowed_commands = {'start', 'stop', 'pause', 'resume', 'status'}
    
    if clean_input not in allowed_commands:
        logger.warning(f"unknown command: {clean_input}")
        return False
    
    return True

def validate_coordinate_range(x: int, y: int, bounds: dict) -> bool:
    """Checks if coordinates fall within the game window."""
    try:
        within_x = bounds['min_x'] <= x <= bounds['max_x']
        within_y = bounds['min_y'] <= y <= bounds['max_y']
        return within_x and within_y
    except KeyError as e:
        logger.error(f"missing bound parameter: {e}")
        return False
    except TypeError:
        logger.error("non-numeric coordinate check attempted")
        return False