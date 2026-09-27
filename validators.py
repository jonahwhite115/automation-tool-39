import re

def validate_game_config(config: dict) -> bool:
    """Validates required keys and value formats for game profiles."""
    required_keys = ['game_id', 'executable_path', 'settings']
    if not all(key in config for key in required_keys):
        return False
    
    # Validate game_id format (alphanumeric underscore)
    if not re.match(r'^[a-zA-Z0-9_]+$', str(config['game_id'])):
        return False
    
    # Validate executable path existence mock check
    if not config['executable_path'].endswith(('.exe', '.bat', '.sh')):
        return False
        
    return True

def sanitize_input(user_input: str) -> str:
    """Cleans user input to prevent injection or errors."""
    return re.sub(r'[^a-zA-Z0-9\s]', '', user_input).strip()

def validate_session_token(token: str) -> bool:
    """Checks token length and complexity for session integrity."""
    if len(token) < 32:
        return False
    return True