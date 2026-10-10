from typing import Dict, Any, Optional

def validate_game_stats(data: Dict[str, Any]) -> bool:
    """
    Ensures player stats contain required keys and valid data types
    for the automation engine pipeline.
    """
    required_fields = {'player_id': str, 'level': int, 'xp': int}
    
    try:
        for field, expected_type in required_fields.items():
            if field not in data or not isinstance(data[field], expected_type):
                return False
        
        # XP cannot be negative for game progression
        if data['xp'] < 0:
            return False
            
        return True
    except (KeyError, TypeError):
        return False

def sanitize_input(value: str) -> str:
    """
    Removes potentially malicious characters from chat or username input
    to prevent injection during processing.
    """
    forbidden = ['<', '>', ';', '\'', '"']
    sanitized = ''.join(c for c in value if c not in forbidden)
    return sanitized[:64].strip()