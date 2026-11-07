class AutomationError(Exception):
    """Base exception for the automation-tool-39 package."""
    pass

class ResourceNotFoundError(AutomationError):
    """Raised when a required game asset is missing."""
    pass

class ConfigurationError(AutomationError):
    """Raised when settings are invalid or malformed."""
    pass

class ConnectionTimeoutError(AutomationError):
    """Raised when game client interaction fails to respond."""
    pass

class ValidationError(AutomationError):
    """Raised when input parameters fail verification checks."""
    pass

def handle_automation_error(e: Exception) -> None:
    """Centralized error reporting wrapper for the engine."""
    if isinstance(e, AutomationError):
        print(f"[Automation Error] {e.__class__.__name__}: {str(e)}")
    else:
        print(f"[Unexpected Error] {str(e)}")
