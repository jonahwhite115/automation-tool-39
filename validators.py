import logging

logger = logging.getLogger(__name__)

def validate_game_config(config: dict) -> bool:
    """Validates automation configuration for gaming scenarios."""
    required_keys = ['account_id', 'target_server', 'max_retries']
    
    try:
        # Check for missing keys in the configuration dictionary
        if not all(key in config for key in required_keys):
            missing = [k for k in required_keys if k not in config]
            raise ValueError(f"Missing required keys: {missing}")

        # Ensure numeric values are within safe operational bounds
        if not isinstance(config.get('max_retries'), int) or config['max_retries'] < 0:
            raise ValueError("max_retries must be a non-negative integer")
            
        if not isinstance(config.get('account_id'), str):
            raise TypeError("account_id must be a string identifier")

        return True

    except (ValueError, TypeError) as e:
        logger.error(f"Configuration validation failure: {e}")
        return False
    except Exception as e:
        logger.critical(f"Unexpected error during validation: {e}")
        return False

def validate_session_status(status_code: int) -> bool:
    """Handles edge cases for session heartbeat connectivity."""
    valid_statuses = {200, 201, 204}
    
    if status_code in valid_statuses:
        return True
    
    if status_code == 403:
        logger.warning("Session forbidden: potential account lockout detected.")
    elif status_code == 429:
        logger.warning("Rate limiting active: cooling down request frequency.")
    else:
        logger.error(f"Unexpected session status encountered: {status_code}")
        
    return False