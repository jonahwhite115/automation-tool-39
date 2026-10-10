import logging

# Input validation rules for game data packets

def validate_game_input(data: dict) -> bool:
    """
    Validates player input structure and value constraints
    before processing in the main loop.
    """
    required_keys = {'player_id', 'action', 'timestamp'}
    
    # Check for missing keys
    if not all(key in data for key in required_keys):
        logging.error("Invalid packet structure received")
        return False
    
    # Validate data types
    if not isinstance(data['player_id'], int):
        return False
        
    # Restrict action commands to allowed set
    allowed_actions = {'move', 'attack', 'interact', 'idle'}
    if data['action'] not in allowed_actions:
        logging.warning(f"Unknown action attempt: {data['action']}")
        return False

    # Timestamp sanity check
    if data['timestamp'] <= 0:
        return False
        
    return True

def sanitize_input(user_input: str) -> str:
    """
    Sanitizes string inputs to prevent injection
    or formatting issues in game logs.
    """
    return str(user_input).strip()[:128]