import re
from typing import Any, Dict

def validate_game_input(data: Dict[str, Any]) -> bool:
    """Validates player commands and integer thresholds for automation.
    
    Ensures coordinates are positive and command strings match
    the expected format for gaming automation inputs.
    """
    required_keys = {'command', 'x', 'y', 'threshold'}
    if not all(key in data for key in required_keys):
        return False

    # Validate command string structure
    if not isinstance(data['command'], str) or not re.match(r'^[A-Z_]{3,15}$', data['command']):
        return False

    # Validate spatial coordinates
    if not all(isinstance(data[k], int) and data[k] >= 0 for k in ['x', 'y']):
        return False

    # Validate sensitivity threshold
    if not isinstance(data['threshold'], (int, float)) or not (0.0 <= data['threshold'] <= 1.0):
        return False

    return True

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """Strip whitespace and normalize keys for processing."""
    return {
        'command': str(data['command']).strip().upper(),
        'x': int(data['x']),
        'y': int(data['y']),
        'threshold': float(data['threshold'])
    }