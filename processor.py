import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class TelemetryProcessingError(Exception):
    """Raised when game telemetry payload is corrupted or unparseable."""
    pass


class TelemetryProcessor:
    """Processes raw gaming telemetry packets with defensive validation."""

    def __init__(self, max_health: int = 100):
        self.max_health = max_health

    def process_packet(self, raw_data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Parse raw telemetry, handling missing values, bad types, and edge cases."""
        if raw_data is None:
            logger.warning("Received empty telemetry packet")
            return {"status": "ignored", "reason": "null_payload"}

        if not isinstance(raw_data, dict):
            raise TelemetryProcessingError(f"Expected dict payload, got {type(raw_data).__name__}")

        player_id = raw_data.get("player_id")
        if not player_id or not isinstance(player_id, (str, int)):
            logger.error("Invalid or missing player_id in telemetry: %s", player_id)
            return {"status": "error", "reason": "invalid_player_id"}

        # Handle non-numeric or out-of-bounds health values
        try:
            raw_health = raw_data.get("health", 0)
            health = float(raw_health)
        except (ValueError, TypeError) as err:
            logger.warning("Unparseable health value '%s' for player %s: %s", raw_data.get("health"), player_id, err)
            health = 0.0

        # Clamp health to valid gaming range [0.0, max_health]
        clamped_health = max(0.0, min(float(self.max_health), health))

        # Safely extract coordinates from nested payloads
        position = raw_data.get("position", {})
        if not isinstance(position, dict):
            logger.warning("Malformed position object for player %s, resetting to origin", player_id)
            position = {}

        try:
            pos_x = float(position.get("x", 0.0))
            pos_y = float(position.get("y", 0.0))
        except (ValueError, TypeError):
            logger.error("Non-numeric coordinates received for player %s", player_id)
            pos_x, pos_y = 0.0, 0.0

        return {
            "status": "success",
            "player_id": str(player_id),
            "health_pct": round((clamped_health / self.max_health) * 100, 2),
            "is_alive": clamped_health > 0,
            "coordinates": {"x": pos_x, "y": pos_y}
        }