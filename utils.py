import math
from typing import Dict, Any, List


def calculate_level_from_xp(xp: int, base_xp: int = 100, exponent: float = 1.5) -> int:
    """
    Calculates the player level based on total XP using an exponential curve.
    """
    if xp < 0:
        raise ValueError("XP cannot be negative")
    if xp == 0:
        return 1
    # Level = (XP / base_xp)^(1/exponent) + 1
    return int(math.pow(xp / base_xp, 1 / exponent)) + 1


def calculate_xp_for_level(level: int, base_xp: int = 100, exponent: float = 1.5) -> int:
    """
    Calculates the minimum cumulative XP required to reach a specific level.
    """
    if level <= 1:
        return 0
    return int(base_xp * math.pow(level - 1, exponent))


def filter_items_by_rarity(inventory: List[Dict[str, Any]], min_rarity: str) -> List[Dict[str, Any]]:
    """
    Filters a list of inventory items by a minimum rarity threshold.
    Rarity hierarchy: common < uncommon < rare < epic < legendary
    """
    rarity_ranks = {
        "common": 1,
        "uncommon": 2,
        "rare": 3,
        "epic": 4,
        "legendary": 5
    }

    min_rank = rarity_ranks.get(min_rarity.lower(), 1)
    filtered_items = []

    for item in inventory:
        item_rarity = item.get("rarity", "common").lower()
        current_rank = rarity_ranks.get(item_rarity, 1)
        if current_rank >= min_rank:
            filtered_items.append(item)

    return filtered_items
