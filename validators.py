import logging

logger = logging.getLogger(__name__)

def validate_game_config(config: dict) -> bool:
    """Validates game automation settings with robust error handling."""
    required_keys = ['game_id', 'click_delay', 'loop_count']
    
    try:
        if not isinstance(config, dict):
            raise ValueError("Configuration must be a dictionary")
            
        for key in required_keys:
            if key not in config:
                raise KeyError(f"Missing required config key: {key}")
        
        if not isinstance(config['click_delay'], (int, float)) or config['click_delay'] < 0:
            raise ValueError("click_delay must be a non-negative number")
            
        if not isinstance(config['loop_count'], int) or config['loop_count'] < -1:
            raise ValueError("loop_count must be an integer or -1 for infinite")
            
        return True
        
    except (KeyError, ValueError, TypeError) as e:
        logger.error(f"Configuration validation failure: {e}")
        return False
    except Exception as e:
        logger.critical(f"Unexpected error during validation: {e}")
        return False

def sanitize_input(value: str) -> str:
    """Ensures input strings are safe for CLI execution."""
    if not isinstance(value, str):
        return ""
    return value.strip().replace(';', '').replace('&', '')