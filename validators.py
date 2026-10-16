import re

class InputValidator:
    """Utility class for validating user-provided game configuration inputs."""

    @staticmethod
    def validate_delay(value: str) -> bool:
        """Ensure input is a positive integer string representing seconds."""
        return value.isdigit() and int(value) > 0

    @staticmethod
    def validate_profile_name(name: str) -> bool:
        """Validate profile name adheres to alphanumeric constraints."""
        return bool(re.match(r"^[a-zA-Z0-9_-]{3,16}$", name))

    @staticmethod
    def validate_hotkey(key: str) -> bool:
        """Verify hotkey is a single alphanumeric character."""
        return len(key) == 1 and key.isalnum()

def get_validated_input(prompt: str, validator_func) -> str:
    """Interactive loop to capture and validate user input."""
    while True:
        user_input = input(f"{prompt}: ").strip()
        if validator_func(user_input):
            return user_input
        print("Invalid input. Please try again.")

# Example usage inside the main processing loop:
# delay = get_validated_input("Enter delay", InputValidator.validate_delay)
# profile = get_validated_input("Enter profile name", InputValidator.validate_profile_name)