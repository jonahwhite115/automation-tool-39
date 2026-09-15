from typing import Dict, Any, Union

def validate_game_stats(data: Dict[str, Any]) -> bool:
    """
    Checks if the game data contains valid score and level fields.
    Expects structure: {'score': int, 'level': int, 'player_id': str}
    """
    required_keys = {'score', 'level', 'player_id'}
    
    if not all(key in data for key in required_keys):
        return False

    # Ensure values are within reasonable gaming bounds
    if not isinstance(data['score'], int) or data['score'] < 0:
        return False

    if not isinstance(data['level'], int) or not (0 < data['level'] < 999):
        return False

    return True

def sanitize_player_input(input_val: Any) -> str:
    """
    Cleans player input to prevent injection in log files.
    """
    clean_val = str(input_val).replace("\n", "").replace("\r", "")
    return clean_val[:128]

def calculate_ranking_tier(score: int) -> str:
    """
    Determines player tier based on score threshold.
    """
    if score > 10000:
        return "legendary"
    elif score > 5000:
        return "diamond"
    elif score > 1000:
        return "gold"
    return "bronze"