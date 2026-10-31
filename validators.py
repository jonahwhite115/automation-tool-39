"""Validation utilities for gaming telemetry and player data payload handling."""

import re
from typing import Any, Dict, List, Tuple

PLAYER_ID_REGEX = re.compile(r"^[a-zA-Z0-9_-]{3,16}$")
VALID_PLATFORMS = {"pc", "ps5", "xbox", "switch", "mobile"}
VALID_ITEM_RARITIES = {"common", "uncommon", "rare", "epic", "legendary"}


def validate_player_id(player_id: str) -> bool:
    """Validate username or player ID format."""
    if not isinstance(player_id, str):
        return False
    return bool(PLAYER_ID_REGEX.match(player_id))


def validate_match_payload(payload: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate incoming match telemetry data payload.

    Returns a tuple of (is_valid, list_of_errors).
    """
    errors = []

    if not isinstance(payload, dict):
        return False, ["Payload must be a dictionary"]

    required_fields = ["match_id", "player_id", "platform", "score", "kills"]
    for field in required_fields:
        if field not in payload:
            errors.append(f"Missing required field: '{field}'")

    if "player_id" in payload and not validate_player_id(str(payload["player_id"])):
        errors.append("Invalid 'player_id' format")

    if "platform" in payload and str(payload["platform"]).lower() not in VALID_PLATFORMS:
        errors.append(f"Invalid platform '{payload.get('platform')}'. Must be one of {VALID_PLATFORMS}")

    if "score" in payload and (not isinstance(payload["score"], (int, float)) or payload["score"] < 0):
        errors.append("Score must be a non-negative number")

    if "kills" in payload and (not isinstance(payload["kills"], int) or payload["kills"] < 0):
        errors.append("Kills must be a non-negative integer")

    return len(errors) == 0, errors


def validate_item_rarity(rarity: str) -> bool:
    """Check if the item rarity string is recognized."""
    if not isinstance(rarity, str):
        return False
    return rarity.lower() in VALID_ITEM_RARITIES
