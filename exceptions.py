"""Custom exceptions and utilities for gaming data handling in automation-tool-39."""

class GamingDataError(Exception):
    """Base exception for all gaming data errors."""
    pass

class InvalidGameDataError(GamingDataError):
    """Raised when provided gaming data is invalid."""
    def __init__(self, message, data_key=None):
        super().__init__(message)
        self.data_key = data_key

class PlayerNotFoundError(GamingDataError):
    """Raised when a player cannot be found in the data."""
    def __init__(self, player_id, message=None):
        if message is None:
            message = "Player data not found"
        super().__init__(f"{message} for ID: {player_id}")
        self.player_id = player_id

class CorruptedSaveDataError(GamingDataError):
    """Raised for corrupted or unreadable save game data."""
    def __init__(self, message, file_path=None):
        super().__init__(message)
        self.file_path = file_path

class InvalidInventoryError(GamingDataError):
    """Raised for invalid player inventory data."""
    pass

class AchievementDataError(GamingDataError):
    """Raised for issues with achievement data."""
    def __init__(self, message, achievement_id=None):
        super().__init__(message)
        self.achievement_id = achievement_id

class ScoreCalculationError(GamingDataError):
    """Raised when calculating scores from game data fails."""
    pass

def validate_gaming_data(data):
    """Validate gaming data dictionary for required fields.
    Practical validation for player stats, inventory etc.
    """
    if not isinstance(data, dict):
        raise InvalidGameDataError("Gaming data must be a dictionary")
    if "player_id" not in data:
        raise PlayerNotFoundError(data.get("player_id", "unknown"))
    if "inventory" in data and not isinstance(data["inventory"], list):
        raise InvalidInventoryError("Inventory must be a list")
    if "score" in data and not isinstance(data["score"], (int, float)):
        raise ScoreCalculationError("Score must be numeric")
    return True

def get_error_details(error):
    """Extract details from a gaming exception for reporting.
    Returns a dict with error info, useful in automation logs.
    """
    details = {
        "error_type": type(error).__name__,
        "message": str(error),
    }
    if isinstance(error, PlayerNotFoundError):
        details["player_id"] = error.player_id
    elif isinstance(error, InvalidGameDataError) and error.data_key:
        details["data_key"] = error.data_key
    elif isinstance(error, CorruptedSaveDataError) and error.file_path:
        details["file_path"] = error.file_path
    elif isinstance(error, AchievementDataError) and error.achievement_id:
        details["achievement_id"] = error.achievement_id
    return details