import re


def validate_player_id(player_id: str) -> bool:
    """Validate gaming platform player ID format."""
    # Pattern: alphanumeric between 4 and 16 characters
    pattern = re.compile(r'^[a-zA-Z0-9]{4,16}$')
    return bool(pattern.match(player_id))


def validate_game_score(score: int) -> bool:
    """Ensure score is within logical game bounds."""
    MIN_SCORE = 0
    MAX_SCORE = 999999
    return MIN_SCORE <= score <= MAX_SCORE


def validate_match_data(data: dict) -> bool:
    """Validate structure of incoming match packets."""
    required_fields = {'match_id', 'player_id', 'score'}
    
    if not all(key in data for key in required_fields):
        return False
        
    if not isinstance(data['score'], int):
        return False
        
    return validate_player_id(data['player_id']) and validate_game_score(data['score'])


def sanitize_chat_message(message: str) -> str:
    """Strip non-printable characters from game chat."""
    # Remove control characters
    return re.sub(r'[\x00-\x1f\x7f-\x9f]', '', message).strip()