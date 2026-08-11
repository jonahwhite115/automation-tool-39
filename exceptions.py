class GameError(Exception):
    """Custom exception for game-related errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class PlayerNotFoundError(GameError):
    """Raised when a specific player is not found."""
    def __init__(self, player_id: str) -> None:
        super().__init__(f'Player with ID {player_id} not found.')
        self.player_id = player_id

class LevelNotLoadedError(GameError):
    """Raised when a game level fails to load."""
    def __init__(self, level_name: str) -> None:
        super().__init__(f'Level {level_name} could not be loaded.')
        self.level_name = level_name

class InvalidInputError(GameError):
    """Raised for invalid inputs in the game."""
    def __init__(self, input_value: str) -> None:
        super().__init__(f'Invalid input: {input_value}')
        self.input_value = input_value