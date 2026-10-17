import logging
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)


class FrameProcessingError(Exception):
    """Raised when telemetry frame data cannot be parsed."""
    pass


class GameStateProcessor:
    """Processes raw gaming telemetry and memory state updates with defensive checks."""

    def __init__(self, max_health: int = 100, max_slots: int = 36):
        self.max_health = max_health
        self.max_slots = max_slots

    def parse_player_stats(self, raw_data: Any) -> Dict[str, Any]:
        """Extract and validate player status payload with fallback handling."""
        if not isinstance(raw_data, dict):
            logger.error(f"Expected dict payload, got {type(raw_data).__name__}")
            return {"health": 0.0, "mana": 0.0, "is_alive": False}

        health = raw_data.get("health")
        mana = raw_data.get("mana", 0)

        try:
            health = float(health) if health is not None else 0.0
            mana = float(mana) if mana is not None else 0.0
        except (ValueError, TypeError):
            logger.warning(f"Invalid stat types encountered in raw payload: {raw_data}")
            health, mana = 0.0, 0.0

        clamped_health = max(0.0, min(health, float(self.max_health)))
        clamped_mana = max(0.0, mana)

        return {
            "health": clamped_health,
            "mana": clamped_mana,
            "is_alive": clamped_health > 0,
        }

    def parse_inventory(self, items_payload: Optional[List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
        """Safely parse inventory items handling missing attributes and slot overflows."""
        if items_payload is None:
            return []

        if not isinstance(items_payload, list):
            logger.warning("Inventory payload is not a list; returning empty inventory")
            return []

        valid_items = []
        for idx, item in enumerate(items_payload):
            if idx >= self.max_slots:
                logger.warning(f"Inventory slot overflow detected at index {idx}")
                break

            if not isinstance(item, dict):
                logger.debug(f"Skipping invalid item entry at index {idx}: {item}")
                continue

            item_id = item.get("id")
            quantity = item.get("quantity", 1)

            if not item_id or not isinstance(item_id, str):
                logger.debug(f"Missing or invalid item ID at slot {idx}")
                continue

            try:
                quantity = int(quantity)
                if quantity <= 0:
                    continue
            except (ValueError, TypeError):
                logger.warning(f"Invalid quantity '{quantity}' for item {item_id}; defaulting to 1")
                quantity = 1

            valid_items.append({"slot": idx, "id": item_id, "quantity": quantity})

        return valid_items
