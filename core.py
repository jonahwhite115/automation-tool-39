import json
from typing import Dict, Any, Optional

def sanitize_game_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Cleans and normalizes incoming gaming session metrics."""
    sanitized = {}
    
    # filter out negative scores or corrupted timestamps
    for key, value in raw_data.items():
        if key == 'score' and isinstance(value, (int, float)):
            sanitized[key] = max(0, value)
        elif key == 'player_id' and isinstance(value, str):
            sanitized[key] = value.strip().lower()
        else:
            sanitized[key] = value
            
    return sanitized

def export_session_log(filepath: str, data: Dict[str, Any]) -> bool:
    """Persists processed session data to local storage."""
    try:
        with open(filepath, 'a') as f:
            f.write(json.dumps(data) + '\n')
        return True
    except (IOError, TypeError):
        return False

def validate_player_payload(data: Dict[str, Any]) -> bool:
    """Ensures required fields exist for backend ingest."""
    required = {'player_id', 'score', 'timestamp'}
    return all(key in data for key in required)