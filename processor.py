import json
from typing import Dict, Any, List

def normalize_game_stats(data: Dict[str, Any]) -> Dict[str, Any]:
    """Sanitizes and normalizes raw gaming session telemetry."""
    processed = {
        "player_id": str(data.get("uid", "unknown")),
        "score": int(data.get("score", 0)),
        "latency_ms": float(data.get("ping", 0.0)),
        "is_active": bool(data.get("status") == "online")
    }
    return processed

def batch_process_stats(raw_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Processes list of telemetry logs into valid schema."""
    results = []
    for entry in raw_data:
        try:
            results.append(normalize_game_stats(entry))
        except (ValueError, TypeError):
            continue
    return results

def serialize_to_json(data: Any, indent: int = 4) -> str:
    """Converts telemetry dictionaries to JSON strings."""
    return json.dumps(data, indent=indent)

if __name__ == "__main__":
    sample = [{"uid": "p123", "score": 1500, "ping": 24.5, "status": "online"}]
    print(serialize_to_json(batch_process_stats(sample)))