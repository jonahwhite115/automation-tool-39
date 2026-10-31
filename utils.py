import json
from typing import Dict, Any, Optional

def sanitize_game_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes sensitive keys and normalizes player stats."""
    sensitive_keys = {'session_token', 'password', 'raw_ip'}
    clean_data = {k: v for k, v in raw_data.items() if k not in sensitive_keys}

    # Normalize stats if present
    if 'xp' in clean_data:
        clean_data['xp'] = int(clean_data['xp'])
    
    return clean_data

def export_to_json(data: Dict[str, Any], file_path: str) -> bool:
    """Serializes game session data to disk."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def calculate_win_rate(wins: int, losses: int) -> float:
    """Safely calculates player win ratio."""
    total = wins + losses
    if total == 0:
        return 0.0
    return round((wins / total) * 100, 2)

def get_session_info(data: Dict[str, Any]) -> str:
    """Formats basic session metadata for logs."""
    player = data.get('username', 'Unknown')
    level = data.get('level', 1)
    return f"Player: {player} | Level: {level}"