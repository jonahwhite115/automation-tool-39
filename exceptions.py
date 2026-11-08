class AutomationError(Exception):
    """Base exception for automation-tool-39."""

class ResourceNotFoundError(AutomationError):
    """Raised when a game asset is missing."""

class ConnectionTimeoutError(AutomationError):
    """Raised when the game process fails to respond."""

class ValidationError(AutomationError):
    """Raised when user configuration is invalid."""

def handle_automation_error(error: Exception) -> None:
    """Standardized logging for internal application exceptions."""
    if isinstance(error, AutomationError):
        print(f"[Automation Error]: {str(error)}")
    else:
        print(f"[Critical System Fault]: {str(error)}")

def validate_resource(resource_path: str) -> bool:
    """Check resource existence with custom exception raising."""
    import os
    if not os.path.exists(resource_path):
        raise ResourceNotFoundError(f"Resource at {resource_path} not found")
    return True