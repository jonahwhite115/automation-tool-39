import re

class InputValidator:
    """Validates user inputs for gaming automation tasks."""

    @staticmethod
    def validate_integer(value, min_val=0, max_val=9999):
        """Ensures input is a valid integer within gaming-specific range."""
        try:
            num = int(value)
            if min_val <= num <= max_val:
                return num
        except (ValueError, TypeError):
            pass
        return None

    @staticmethod
    def validate_command(command):
        """Sanitizes command strings to prevent shell injection."""
        # Allow only alphanumeric, spaces, and standard gaming keys
        if command and re.match(r'^[a-zA-Z0-9\s]{1,32}$', command):
            return command.strip()
        return None

    @staticmethod
    def validate_coordinates(x, y):
        """Checks if coordinate pairs are within screen resolution bounds."""
        try:
            ix, iy = int(x), int(y)
            if 0 <= ix <= 3840 and 0 <= iy <= 2160:
                return (ix, iy)
        except (ValueError, TypeError):
            pass
        return None