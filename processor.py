import json
from typing import Dict, Any, Optional

def normalize_game_stats(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    standardizes player performance metrics from raw telemetry
    """
    normalized = {
        "player_id": data.get("uid", "unknown"),
        "score": int(data.get("points", 0)),
        "kda": float(data.get("kills", 0)) / max(1, int(data.get("deaths", 1))),
        "is_active": data.get("status") == "online"
    }
    return normalized

def save_session_data(filepath: str, data: Dict[str, Any]) -> bool:
    """
    persistence layer for gaming session payloads
    """
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError) as e:
        print(f"serialization failure: {e}")
        return False

def parse_match_payload(raw_json: str) -> Optional[Dict[str, Any]]:
    """
    safe parsing for external match data packets
    """
    try:
        payload = json.loads(raw_json)
        return payload if isinstance(payload, dict) else None
    except json.JSONDecodeError:
        return None