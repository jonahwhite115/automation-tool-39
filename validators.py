from typing import List, Optional, Union

def validate_game_id(game_id: Union[int, str]) -> bool:
    """Checks if provided game identifier is valid.

    Args:
        game_id: The game identifier to check.

    Returns:
        bool: True if identifier is valid, False otherwise.
    """
    if isinstance(game_id, int):
        return game_id > 0
    return isinstance(game_id, str) and len(game_id) > 0

def validate_player_list(players: List[str], max_size: int = 10) -> bool:
    """Validates player list constraints for gaming sessions.

    Args:
        players: List of unique player usernames.
        max_size: Maximum allowed players in session.

    Returns:
        bool: True if player list is valid.
    """
    if not players or len(players) > max_size:
        return False
    return len(set(players)) == len(players)

def sanitize_config_path(path: Optional[str]) -> str:
    """Ensures configuration path is normalized.

    Args:
        path: Raw path string from input.

    Returns:
        str: Sanitized path or default path.
    """
    if not path or not isinstance(path, str):
        return "default_config.json"
    return path.strip().replace("\\", "/")