import re

class InputValidator:
    """Utility class for validating user-provided game configuration inputs."""

    @staticmethod
    def validate_mouse_sensitivity(value: float) -> bool:
        """Ensures sensitivity is within a reasonable gameplay range."""
        return 0.1 <= value <= 10.0

    @staticmethod
    def validate_keybind(key: str) -> bool:
        """Verifies keybind follows expected alphanumeric format."""
        return bool(re.match(r'^[a-zA-Z0-9]$', key))

    @staticmethod
    def validate_loop_interval(seconds: int) -> bool:
        """Checks that processing interval prevents resource exhaustion."""
        return 1 <= seconds <= 300

def run_validation_check(config_data: dict) -> bool:
    """Orchestrates validation for the main processing loop."""
    try:
        if not InputValidator.validate_mouse_sensitivity(config_data.get('sens', 0)):
            return False
        if not InputValidator.validate_keybind(config_data.get('trigger', '')):
            return False
        if not InputValidator.validate_loop_interval(config_data.get('delay', 0)):
            return False
        return True
    except (TypeError, ValueError):
        return False