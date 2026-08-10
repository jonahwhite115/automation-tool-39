class CustomError(Exception):
    """Custom exception for general errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, field: str, message: str) -> None:
        super().__init__(message)
        self.field = field

    def __str__(self) -> str:
        return f'Validation error in field {self.field}: {self.message}'

class NotFoundError(CustomError):
    """Exception raised when an item is not found."""
    def __init__(self, item_id: str) -> None:
        message = f'Item with ID {item_id} not found.'
        super().__init__(message)
        self.item_id = item_id

    def __str__(self) -> str:
        return self.message

class UnauthorizedError(CustomError):
    """Exception raised for unauthorized access."""
    def __init__(self) -> None:
        message = 'Unauthorized access attempted.'
        super().__init__(message)

    def __str__(self) -> str:
        return self.message
