class GameError(Exception):
    """Base class for exceptions in the gaming module."""
    pass

class PlayerError(GameError):
    """Exception raised for errors related to player actions."""
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

class GameLoadError(GameError):
    """Exception raised when a game fails to load."""
    def __init__(self, game_name: str) -> None:
        self.game_name = game_name
        self.message = f'Failed to load game: {game_name}'
        super().__init__(self.message)

class InvalidInputError(GameError):
    """Exception raised for invalid input provided by the user."""
    def __init__(self, input_value: str) -> None:
        self.input_value = input_value
        self.message = f'Invalid input: {input_value}'
        super().__init__(self.message)