import re
from typing import Any, Optional

# Gaming asset validation constants
MAX_GAMERTAG_LENGTH = 16
ID_PATTERN = re.compile(r'^[a-zA-Z0-9_-]+$')

class ValidationError(Exception):
    """Custom exception for validation failures."""
    pass

def validate_gamertag(name: str) -> bool:
    """Ensures gamertag follows community guidelines."""
    if not name or len(name) > MAX_GAMERTAG_LENGTH:
        return False
    return bool(ID_PATTERN.match(name))

def validate_server_region(region: str) -> bool:
    """Verifies region string is within supported zones."""
    supported_regions = {'na-east', 'na-west', 'eu-central', 'asia-east'}
    return region.lower() in supported_regions

def sanitize_input(data: Any) -> Optional[str]:
    """Strips whitespace and ensures string format."""
    if not isinstance(data, str):
        return None
    return data.strip()