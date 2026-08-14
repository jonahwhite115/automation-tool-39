from typing import List, Dict, Any


def calculate_player_score(player_data: Dict[str, Any]) -> int:
    """
    Calculate the total score for a player based on their game statistics.

    Args:
        player_data (Dict[str, Any]): A dictionary containing player's data including scores.

    Returns:
        int: The total score for the player.
    """
    total_score = 0
    for score in player_data.get('scores', []):
        total_score += score
    return total_score


def filter_high_scores(scores: List[int], threshold: int) -> List[int]:
    """
    Filter scores above a specified threshold.

    Args:
        scores (List[int]): A list of scores to filter.
        threshold (int): The score threshold.

    Returns:
        List[int]: A list of scores that are greater than the threshold.
    """
    high_scores = [score for score in scores if score > threshold]
    return high_scores


def sort_player_scores(scores: List[int], reverse: bool = False) -> List[int]:
    """
    Sort a list of player scores in ascending or descending order.

    Args:
        scores (List[int]): A list of scores to sort.
        reverse (bool): Whether to sort in descending order. Defaults to False.

    Returns:
        List[int]: A sorted list of scores.
    """
    return sorted(scores, reverse=reverse)
