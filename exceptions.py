class GameError(Exception):
    """
    Custom exception for game-related errors.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class InvalidMoveError(GameError):
    """
    Exception raised for invalid moves in the game.
    """  
    def __init__(self, move: str) -> None:
        super().__init__(f"Invalid move: {move}")
        self.move = move

class GameNotStartedError(GameError):
    """
    Exception raised when an action is attempted before the game starts.
    """  
    def __init__(self) -> None:
        super().__init__("Game has not started yet.")

class PlayerAlreadyJoinedError(GameError):
    """
    Exception raised when a player tries to join an already joined game.
    """  
    def __init__(self, player_name: str) -> None:
        super().__init__(f"Player '{player_name}' has already joined.")
        self.player_name = player_name

class InsufficientResourcesError(GameError):
    """
    Exception raised when resources are insufficient for an action.
    """  
    def __init__(self, required: int, available: int) -> None:
        super().__init__(f"Insufficient resources: required {required}, available {available}")
        self.required = required
        self.available = available
