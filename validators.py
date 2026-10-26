import re

def validate_game_id(game_id: str) -> bool:
    """Checks if game ID follows the expected alphanumeric format."""
    pattern = r'^[a-z0-9_-]{3,32}$'
    return bool(re.match(pattern, game_id))

def validate_settings(settings: dict) -> bool:
    """Verifies existence of mandatory automation configuration keys."""
    required = ['resolution', 'fps_limit', 'save_path']
    return all(key in settings for key in required)

def validate_memory_address(address: str) -> bool:
    """Validates hexadecimal format for memory manipulation."""
    try:
        int(address, 16)
        return len(address) >= 4
    except ValueError:
        return False

def sanitize_input(value: str) -> str:
    """Removes potentially malicious control characters."""
    return re.sub(r'[\x00-\x1f\x7f]', '', value)

def check_bounds(value: int, min_val: int, max_val: int) -> bool:
    """Ensures numerical settings stay within physical bounds."""
    return min_val <= value <= max_val