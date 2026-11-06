from typing import Dict, List, Any


def calculate_player_metrics(match_data: Dict[str, Any]) -> Dict[str, float]:
    """
    Calculate performance metrics from raw gaming match telemetry.
    Returns K/D ratio, score per minute, and kill participation.
    """
    kills = match_data.get("kills", 0)
    deaths = match_data.get("deaths", 0)
    score = match_data.get("score", 0)
    duration_seconds = match_data.get("duration_seconds", 1)
    team_kills = match_data.get("team_kills", kills)

    # Prevent division by zero
    kd_ratio = round(kills / max(1, deaths), 2)
    duration_minutes = max(0.1, duration_seconds / 60.0)
    spm = round(score / duration_minutes, 2)

    kill_part = 0.0
    if team_kills > 0:
        kill_part = round((kills / team_kills) * 100, 1)

    return {
        "kd_ratio": kd_ratio,
        "score_per_minute": spm,
        "kill_participation": kill_part,
    }


def filter_inventory_by_rarity(
    inventory: List[Dict[str, Any]], min_rarity: str
) -> List[Dict[str, Any]]:
    """
    Filter player inventory items by a minimum required rarity tier.
    """
    rarity_tiers = ["common", "uncommon", "rare", "epic", "legendary", "mythic"]
    target = min_rarity.lower()

    if target not in rarity_tiers:
        return inventory

    threshold = rarity_tiers.index(target)
    result = []

    for item in inventory:
        item_tier = item.get("rarity", "").lower()
        if item_tier in rarity_tiers and rarity_tiers.index(item_tier) >= threshold:
            result.append(item)

    return result
