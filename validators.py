import re

class InputValidator:
    @staticmethod
    def is_valid_username(username: str) -> bool:
        # Check if username matches the regex pattern
        pattern = r'^[A-Za-z0-9_]{3,15}$'
        return re.match(pattern, username) is not None

    @staticmethod
    def is_valid_password(password: str) -> bool:
        # Check for a valid password (at least 8 characters, one uppercase, one digit)
        if len(password) < 8:
            return False
        return (
            re.search(r'[A-Z]', password) is not None and
            re.search(r'[0-9]', password) is not None
        )

    @staticmethod
    def validate_email(email: str) -> bool:
        # Simple email validation using regex
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_game_score(score: int) -> bool:
        # Ensure score is a positive integer
        return isinstance(score, int) and score >= 0

# Example usage
if __name__ == '__main__':
    print(InputValidator.is_valid_username('Player123'))  # True
    print(InputValidator.is_valid_password('Password1'))  # True
    print(InputValidator.validate_email('user@example.com'))  # True
    print(InputValidator.validate_game_score(100))  # True
