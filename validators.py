import re

class InputValidator:
    """Utility class for validating user-provided game configuration inputs."""

    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        """Check if user_id follows standard alphanumeric pattern."""
        return bool(re.match(r'^[a-zA-Z0-9_]{3,16}$', user_id))

    @staticmethod
    def validate_action_delay(delay: int) -> bool:
        """Ensure action delay is within reasonable game-safe bounds."""
        return 50 <= delay <= 5000

    @staticmethod
    def validate_macro_key(key: str) -> bool:
        """Verify that the provided key is a single valid character."""
        return len(key) == 1 and key.isalnum()

def process_input(user_input: dict):
    """Main loop entry for input validation processing."""
    validator = InputValidator()
    
    # Validate individual components of the game automation config
    if not validator.validate_user_id(user_input.get('user', '')):
        raise ValueError("Invalid user ID format")
        
    if not validator.validate_action_delay(user_input.get('delay', 0)):
        raise ValueError("Delay must be between 50 and 5000ms")
        
    if not validator.validate_macro_key(user_input.get('key', '')):
        raise ValueError("Macro trigger must be a single alphanumeric key")
        
    return True