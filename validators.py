from typing import Any, Dict, List, Optional
import re

def validate_player_id(player_id: str) -> bool:
    """Validate player ID for gaming automation.
    Must be 8-16 alphanumeric chars.
    Args:
        player_id: The ID to check.
    Returns:
        True if valid.
    """
    if not isinstance(player_id, str):
        return False
    return bool(re.match(r'^[a-zA-Z0-9]{8,16}$', player_id))

def validate_score(score: int) -> bool:
    """Validate game score.
    Must be int between 0 and 1e6.
    Args:
        score: Score value.
    Returns:
        True if valid.
    """
    if not isinstance(score, int):
        return False
    return 0 <= score <= 1000000

def validate_config(config: Dict[str, Any]) -> bool:
    """Validate gaming config dict.
    Requires difficulty, num_players, auto_save with valid values.
    Args:
        config: Settings dict.
    Returns:
        True if valid.
    """
    if not isinstance(config, dict):
        return False
    if 'difficulty' not in config or config['difficulty'] not in ['easy', 'medium', 'hard']:
        return False
    if 'num_players' not in config or not isinstance(config['num_players'], int) or not 1 <= config['num_players'] <= 4:
        return False
    if 'auto_save' not in config or not isinstance(config['auto_save'], bool):
        return False
    return True

def validate_input_commands(commands: List[str]) -> bool:
    """Validate game input commands list.
    Commands from predefined valid set.
    Args:
        commands: List of str commands.
    Returns:
        True if all valid.
    """
    if not isinstance(commands, list):
        return False
    valid = {'move_up', 'move_down', 'move_left', 'move_right', 'attack', 'defend', 'special'}
    return all(isinstance(cmd, str) and cmd in valid for cmd in commands)

def validate_player_data(data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Validate player data dict.
    Returns cleaned data or None.
    Args:
        data: Player info.
    Returns:
        Cleaned dict or None.
    """
    if not isinstance(data, dict):
        return None
    username = data.get('username', '')
    if not isinstance(username, str) or len(username) < 3 or len(username) > 20 or not re.match(r'^[a-zA-Z0-9_]+$', username):
        return None
    score = data.get('score', 0)
    if not isinstance(score, int) or score < 0 or score > 1000000:
        return None
    level = data.get('level', 1)
    if not isinstance(level, int) or level < 1 or level > 100:
        return None
    return {'username': username, 'score': score, 'level': level}
