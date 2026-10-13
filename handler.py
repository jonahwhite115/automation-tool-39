import json
from typing import Dict, List, Any, Optional

class GameDataHandler:
    """Utility for parsing and sanitizing gaming telemetry data."""

    def __init__(self, schema_version: str = "1.0"):
        self.version = schema_version

    def validate_payload(self, data: Dict[str, Any]) -> bool:
        """Checks if required gaming keys exist."""
        required = ["player_id", "session_id", "score"]
        return all(key in data for key in required)

    def process_telemetry(self, raw_data: str) -> Optional[Dict[str, Any]]:
        """Parses JSON string and applies versioning context."""
        try:
            data = json.loads(raw_data)
            if self.validate_payload(data):
                data["processed_at_version"] = self.version
                return data
        except (json.JSONDecodeError, TypeError):
            return None
        return None

    def aggregate_scores(self, data_list: List[Dict[str, Any]]) -> int:
        """Summation of player scores from provided list."""
        return sum(item.get("score", 0) for item in data_list)

if __name__ == "__main__":
    handler = GameDataHandler()
    sample = '{"player_id": "p1", "session_id": "s1", "score": 150}'
    result = handler.process_telemetry(sample)
    print(f"Processed result: {result}")