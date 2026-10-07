class AutomationError(Exception):
    """Base exception for all automation-tool-39 errors."""
    pass

class GameProcessError(AutomationError):
    """Raised when the game process cannot be accessed."""
    pass

class ConfigurationError(AutomationError):
    """Raised when settings are invalid or missing."""
    pass

class InputInjectionError(AutomationError):
    """Raised when keyboard or mouse simulation fails."""
    pass

class PixelDetectionError(AutomationError):
    """Raised when visual scanning fails to find targets."""
    pass

def handle_exception(exc: Exception):
    """Format and log custom automation exceptions."""
    if isinstance(exc, AutomationError):
        print(f"[Automation Error] {type(exc).__name__}: {exc}")
    else:
        print(f"[Critical System Error] {exc}")

def validate_game_state(condition: bool, message: str):
    """Check game state and raise specific exception if false."""
    if not condition:
        raise GameProcessError(message)