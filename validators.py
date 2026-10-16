import re
from typing import Any, Optional

def validate_input_data(data: Any, min_val: int = 0, max_val: int = 9999) -> bool:
    """Ensures game configuration values are within expected bounds."""
    if not isinstance(data, int):
        return False
    return min_val <= data <= max_val

def validate_player_name(name: str) -> bool:
    """Validates player aliases using regex patterns."""
    if not isinstance(name, str) or len(name) < 3:
        return False
    pattern = re.compile(r"^[a-zA-Z0-9_-]+$")
    return bool(pattern.match(name))

def sanitize_config_key(key: str) -> Optional[str]:
    """Removes illegal characters from configuration keys."""
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '', key)
    return sanitized if sanitized else None

# Usage in main loop:
# def process_tick(payload):
#     if validate_input_data(payload['ticks']) and validate_player_name(payload['name']):
#         execute_action(payload)
#     else:
#         log_error('invalid input detected')