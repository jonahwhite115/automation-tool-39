from typing import Dict, Any, Union

def validate_game_state(data: Dict[str, Any]) -> bool:
    """Validates player session data structure."""
    required_keys = {'player_id', 'level', 'score', 'timestamp'}
    
    if not isinstance(data, dict):
        return False
        
    if not required_keys.issubset(data.keys()):
        return False
        
    if data['score'] < 0:
        return False
        
    return True

def sanitize_input_metrics(metrics: Dict[str, Union[int, float]]) -> Dict[str, Union[int, float]]:
    """Filters negative values from game metrics."""
    return {k: max(0, v) for k, v in metrics.items() if isinstance(v, (int, float))}

def check_bounds(value: float, min_val: float, max_val: float) -> float:
    """Clamps coordinate values for game map bounds."""
    return max(min_val, min(value, max_val))

def parse_server_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Extracts and cleans game event data."""
    return {
        "id": str(payload.get("uuid", "unknown")),
        "active": bool(payload.get("status", False)),
        "latency": float(payload.get("ping", 0.0))
    }