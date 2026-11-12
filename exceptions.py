class GamingAutomationError(Exception):
    """Base exception for automation-tool-39 operations."""
    pass

class DataParsingError(GamingAutomationError):
    """Raised when raw game data cannot be decoded."""
    pass

class ResourceNotFoundError(GamingAutomationError):
    """Raised when a game entity cannot be located."""
    pass

class StateTransitionError(GamingAutomationError):
    """Raised when an invalid game state occurs."""
    def __init__(self, current_state, target_state):
        super().__init__(f"Cannot transition from {current_state} to {target_state}")

def validate_game_payload(payload: dict):
    """Ensures incoming data contains required keys for processing."""
    required_keys = {"session_id", "timestamp", "action_type"}
    if not required_keys.issubset(payload.keys()):
        missing = required_keys - payload.keys()
        raise DataParsingError(f"Payload missing required fields: {missing}")
    return True