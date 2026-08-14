class GameError(Exception):
    """Base class for exceptions in the game module."""
    def __init__(self, message):
        super().__init__(message)

class InvalidMoveError(GameError):
    """Raised when an invalid move is attempted."""
    def __init__(self, move):
        message = f"Invalid move attempted: {move}"
        super().__init__(message)

class PlayerNotFoundError(GameError):
    """Raised when a player is not found in the game."""
    def __init__(self, player_name):
        message = f"Player not found: {player_name}"
        super().__init__(message)

class GameAlreadyStartedError(GameError):
    """Raised when an action is attempted after the game has started."""
    def __init__(self):
        message = "Cannot perform action: game has already started"
        super().__init__(message)

class InsufficientResourcesError(GameError):
    """Raised when there are not enough resources for an action."""
    def __init__(self, needed, available):
        message = f"Insufficient resources: needed {needed}, available {available}"
        super().__init__(message)