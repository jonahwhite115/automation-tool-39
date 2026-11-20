import re

class InputValidator:
    """Utility to ensure gaming automation inputs meet safety constraints."""

    @staticmethod
    def validate_coordinates(x: int, y: int) -> bool:
        """Verify screen coordinates are within standard 4K bounds."""
        if 0 <= x <= 3840 and 0 <= y <= 2160:
            return True
        return False

    @staticmethod
    def validate_delay(delay: float) -> bool:
        """Ensure input delay is within a safe range (0 to 10 seconds)."""
        return 0 <= delay <= 10.0

    @staticmethod
    def validate_action_name(name: str) -> bool:
        """Check that action identifiers only contain alphanumeric characters."""
        if not name or len(name) > 32:
            return False
        return bool(re.match(r'^[a-zA-Z0-9_]+$', name))

def get_validated_input(data: dict):
    """Bulk validation for automation processing loop."""
    x = data.get('x', -1)
    y = data.get('y', -1)
    delay = data.get('delay', -1)
    action = data.get('action', '')

    if not InputValidator.validate_coordinates(x, y):
        raise ValueError(f"Invalid coordinates: {x}, {y}")

    if not InputValidator.validate_delay(delay):
        raise ValueError(f"Invalid delay: {delay}")

    if not InputValidator.validate_action_name(action):
        raise ValueError(f"Invalid action name: {action}")

    return True