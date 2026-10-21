import logging

# Configuration for gaming automation input bounds
MIN_INTERVAL = 0.5
MAX_INTERVAL = 60.0
ALLOWED_KEYS = {'w', 'a', 's', 'd', 'space', 'shift', 'ctrl'}

logger = logging.getLogger(__name__)

def validate_input_sequence(sequence: list) -> bool:
    """Validates game input sequence parameters before execution."""
    if not isinstance(sequence, list):
        logger.error("Input sequence must be a list")
        return False

    for entry in sequence:
        action = entry.get('action')
        duration = entry.get('duration', 0)

        if action not in ALLOWED_KEYS:
            logger.warning(f"Invalid action detected: {action}")
            return False

        if not isinstance(duration, (int, float)) or not (MIN_INTERVAL <= duration <= MAX_INTERVAL):
            logger.warning(f"Duration {duration} out of bounds [{MIN_INTERVAL}, {MAX_INTERVAL}]")
            return False

    return True

def sanitize_coords(x: int, y: int, screen_width: int, screen_height: int) -> tuple:
    """Ensures screen coordinates remain within bounds."""
    safe_x = max(0, min(x, screen_width))
    safe_y = max(0, min(y, screen_height))
    return (safe_x, safe_y)