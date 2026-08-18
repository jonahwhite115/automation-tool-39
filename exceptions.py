class GameError(Exception):
    """Base class for exceptions in the gaming module."""
    pass

class PlayerNotFoundError(GameError):
    """Raised when a player is not found."""
    def __init__(self, player_id):
        super().__init__(f'Player with ID {player_id} not found.')
        self.player_id = player_id

class InvalidMoveError(GameError):
    """Raised when a move is invalid."""
    def __init__(self, move):
        super().__init__(f'Invalid move: {move}')
        self.move = move

class GameOverError(GameError):
    """Raised when an operation is attempted after the game is over."""
    def __init__(self):
          super().__init__('Operation not allowed: Game is already over.')

class ConnectionError(GameError):
    """Raised when there is a connection issue."""
    def __init__(self, message):
        super().__init__(message)