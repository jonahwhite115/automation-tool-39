import re
from typing import Any, Optional

def validate_game_id(game_id: str) -> bool:
    """Checks if game_id follows standard hex format."""
    pattern = re.compile(r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$')
    return bool(pattern.match(game_id))

def validate_player_count(count: Any) -> int:
    """Ensures player count is within game capacity bounds."""
    try:
        value = int(count)
        if 1 <= value <= 128:
            return value
        raise ValueError('Count out of bounds')
    except (ValueError, TypeError):
        return 0

def validate_session_token(token: Optional[str]) -> bool:
    """Validates session token length and character safety."""
    if not token or len(token) < 32:
        return False
    return token.isalnum()

def sanitize_player_name(name: str) -> str:
    """Removes illegal characters from player aliases."""
    return re.sub(r'[^a-zA-Z0-9_-]', '', name)[:16]