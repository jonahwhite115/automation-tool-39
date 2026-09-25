import json
from typing import Dict, List, Any, Optional

def parse_game_data(raw_data: str) -> Optional[Dict[str, Any]]:
    """Parses gaming JSON strings and validates structure."""
    try:
        data = json.loads(raw_data)
        if not isinstance(data, dict) or "player_id" not in data:
            return None
        return data
    except (json.JSONDecodeError, TypeError):
        return None

def calculate_stat_averages(sessions: List[Dict[str, Any]]) -> Dict[str, float]:
    """Aggregates performance metrics from session list."""
    if not sessions:
        return {"avg_score": 0.0, "avg_latency": 0.0}
    
    total_score = sum(s.get("score", 0) for s in sessions)
    total_latency = sum(s.get("latency", 0) for s in sessions)
    count = len(sessions)
    
    return {
        "avg_score": total_score / count,
        "avg_latency": total_latency / count
    }

def format_player_payload(player_id: str, stats: Dict[str, Any]) -> str:
    """Serializes processed stats for transmission."""
    payload = {
        "player_id": player_id,
        "metrics": stats,
        "status": "processed"
    }
    return json.dumps(payload)