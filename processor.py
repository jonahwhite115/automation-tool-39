import random
from typing import List, Dict, Any


def calculate_score(player_stats: Dict[str, Any]) -> int:
    """Calculate the score based on player statistics."""
    base_score = player_stats.get('base_score', 0)
    level_multiplier = player_stats.get('level', 1) * 10
    score = base_score + level_multiplier
    return score


def select_random_item(items: List[str]) -> str:
    """Select a random item from a list of items."""
    if not items:
        raise ValueError('Item list cannot be empty')
    return random.choice(items)


def filter_active_players(players: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filter out players who are not active."""
    return [player for player in players if player.get('active', False)]


def log_player_action(player_id: str, action: str) -> None:
    """Log a specific action taken by a player."""
    print(f'Player {player_id} performed action: {action}')