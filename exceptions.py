class AutomationError(Exception):
    """Base exception class for automation-tool-39."""
    pass

class GameSessionError(AutomationError):
    """Raised when game interaction fails."""
    pass

class ConfigurationError(AutomationError):
    """Raised when config files are invalid."""
    pass

class ProcessNotFoundError(AutomationError):
    """Raised when the target game process is missing."""
    pass

class ResourceLimitError(AutomationError):
    """Raised when system resources are exhausted."""
    pass

def handle_exception(e: Exception) -> None:
    """Standardized exception reporting for game automation modules."""
    if isinstance(e, AutomationError):
        print(f"[Automation Error]: {str(e)}")
    else:
        print(f"[Critical System Error]: {type(e).__name__} - {str(e)}")