import logging

logger = logging.getLogger(__name__)

def validate_game_config(config: dict) -> bool:
    """Validates game configuration keys and value constraints."""
    required_keys = ['resolution', 'fps_cap', 'server_region']
    
    try:
        if not isinstance(config, dict):
            raise ValueError("Configuration must be a dictionary")
            
        for key in required_keys:
            if key not in config:
                raise KeyError(f"Missing required configuration: {key}")
        
        if not (30 <= config.get('fps_cap', 0) <= 240):
            logger.warning("fps_cap outside standard range, clamping applied")
            config['fps_cap'] = max(30, min(240, config['fps_cap']))
            
        return True
        
    except (ValueError, KeyError, TypeError) as e:
        logger.error(f"validation failure: {e}")
        return False

def sanitize_input(user_input: str) -> str:
    """Cleans raw input to prevent injection in gaming commands."""
    if not isinstance(user_input, str):
        return ""
    
    # Remove potential control characters and whitespace
    sanitized = "".join(char for char in user_input if char.isalnum() or char in [' ', '_'])
    return sanitized.strip()[:32]