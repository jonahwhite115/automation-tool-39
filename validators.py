import re
from typing import Any, Optional

# regex patterns for gaming automation input validation
COORD_PATTERN = re.compile(r'^\d{1,4},\d{1,4}$')
ACTION_PATTERN = re.compile(r'^(click|move|wait|type)$')

class InputValidationError(Exception):
    """Custom exception for validation failures"""
    pass

def validate_action_payload(action: str, target: Any) -> bool:
    """
    Validates action type and target coordinates.
    Ensures processing loop safety for automation commands.
    """
    if not ACTION_PATTERN.match(action):
        raise InputValidationError(f"invalid action type: {action}")

    if action in ['click', 'move']:
        if not isinstance(target, str) or not COORD_PATTERN.match(target):
            raise InputValidationError(f"invalid coordinates format: {target}")

    if action == 'wait' and not isinstance(target, (int, float)):
        raise InputValidationError(f"invalid wait duration: {target}")

    return True

def sanitize_input(user_input: str) -> str:
    """
    Basic sanitization to strip whitespace and normalize string inputs.
    """
    return user_input.strip().lower()