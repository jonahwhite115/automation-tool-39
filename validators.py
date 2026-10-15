import re


def validate_player_id(player_id: str) -> bool:
    """Validate gaming platform user ID format."""
    # Matches alphanumeric, 3-16 chars
    pattern = re.compile(r'^[a-zA-Z0-9_]{3,16}$')
    return bool(pattern.match(player_id))


def validate_score_range(score: int, min_val: int = 0, max_val: int = 1000000) -> bool:
    """Ensure game score is within realistic bounds."""
    return min_val <= score <= max_val


def sanitize_game_metadata(data: dict) -> dict:
    """Clean dictionary keys and ensure valid types."""
    sanitized = {}
    for key, value in data.items():
        # Remove non-alphanumeric chars from keys
        clean_key = re.sub(r'[^a-zA-Z0-9_]', '', str(key))
        if isinstance(value, (int, float, str, bool)):
            sanitized[clean_key] = value
    return sanitized


def validate_region_code(code: str) -> bool:
    """Check if region code follows ISO-like standard."""
    regions = {'US', 'EU', 'AP', 'LATAM', 'CN'}
    return code.upper() in regions