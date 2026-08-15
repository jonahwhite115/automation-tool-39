class GameError(Exception):
    """Base class for exceptions in the game."""
    pass

class ConfigurationError(GameError):
    """Raised when there is a configuration error."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InvalidInputError(GameError):
    """Raised for invalid inputs from users."""
    def __init__(self, input_value):
        super().__init__(f'Invalid input: {input_value}')
        self.input_value = input_value

class ResourceNotFoundError(GameError):
    """Raised when a resource is not found."""
    def __init__(self, resource_name):
        super().__init__(f'Resource not found: {resource_name}')
        self.resource_name = resource_name

class NetworkError(GameError):
    """Raised for network-related issues."""
    def __init__(self, status_code):
        super().__init__(f'Network error with status code: {status_code}')
        self.status_code = status_code
