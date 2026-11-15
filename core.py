import json
from typing import Dict, Any, Optional

def parse_game_session(raw_data: str) -> Dict[str, Any]:
    """Parses raw gaming session JSON with schema validation."""
    try:
        data = json.loads(raw_data)
        required = ['session_id', 'player_id', 'score']
        if not all(k in data for k in required):
            raise ValueError(f"Missing required session keys: {required}")
        return data
    except (json.JSONDecodeError, TypeError) as e:
        return {"error": str(e), "status": "invalid"}

def calculate_win_rate(wins: int, losses: int) -> float:
    """Calculates win percentage, handles division by zero."""
    total = wins + losses
    if total == 0:
        return 0.0
    return round((wins / total) * 100, 2)

def format_player_stats(player_id: str, data: Dict[str, Any]) -> str:
    """Formats player metrics for console output."""
    stats = data.get("stats", {})
    return f"Player {player_id}: {stats.get('level', 0)} XP"
