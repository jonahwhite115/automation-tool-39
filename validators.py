import re
from typing import Any, Dict, Optional

def validate_player_stats(stats: Dict[str, Any]) -> bool:
    """Validate game statistics structure for consistency."""
    required_keys = {"player_id", "level", "xp", "inventory"}
    if not isinstance(stats, dict) or not required_keys.issubset(stats.keys()):
        return False
    
    # Ensure numerical values are positive
    if stats["level"] < 0 or stats["xp"] < 0:
        return False
        
    return True

def sanitize_username(username: str) -> Optional[str]:
    """Clean username string to prevent injection or invalid chars."""
    if not username or len(username) > 16:
        return None
    
    # Allow alphanumeric and underscores only
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    if not pattern.match(username):
        return None
        
    return username

def validate_game_config(config: Dict[str, Any]) -> bool:
    """Check if configuration keys are present and typed correctly."""
    expected = {"max_players": int, "region": str, "enable_cheats": bool}
    
    for key, expected_type in expected.items():
        val = config.get(key)
        if val is None or not isinstance(val, expected_type):
            return False
    return True