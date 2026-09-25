import json
from typing import Dict, Any, Optional

def parse_game_session(raw_data: str) -> Optional[Dict[str, Any]]:
    """Parses raw JSON game session strings into valid dictionaries."""
    try:
        data = json.loads(raw_data)
        if isinstance(data, dict) and 'session_id' in data:
            return data
        return None
    except (json.JSONDecodeError, TypeError):
        return None

def sanitize_player_metrics(metrics: Dict[str, Any]) -> Dict[str, float]:
    """Converts all numerical values in metrics to standard floats."""
    sanitized = {}
    for key, value in metrics.items():
        try:
            sanitized[key] = float(value)
        except (ValueError, TypeError):
            continue
    return sanitized

def format_session_summary(session_data: Dict[str, Any]) -> str:
    """Creates a human-readable summary from session dictionary."""
    sid = session_data.get('session_id', 'unknown')
    score = session_data.get('score', 0)
    return f"Session {sid} ended with score {score}"