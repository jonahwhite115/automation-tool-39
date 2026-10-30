class AutomationError(Exception):
    """Base exception for all automation-tool-39 errors."""
    pass

class GameProcessError(AutomationError):
    """Raised when the game process is inaccessible."""
    pass

class ConfigValidationError(AutomationError):
    """Raised when configuration files are invalid."""
    pass

class NetworkTimeoutError(AutomationError):
    """Raised when remote server requests time out."""
    pass

class ResourceAccessError(AutomationError):
    """Raised when file or memory handles fail."""
    pass

def handle_exception(e: Exception) -> None:
    """Centralized error reporting logic."""
    if isinstance(e, AutomationError):
        print(f"[Automation Error]: {e}")
    else:
        print(f"[Unexpected System Error]: {str(e)}")

class ErrorFactory:
    """Factory for standardized error instantiation."""
    @staticmethod
    def create_process_error(pid: int) -> GameProcessError:
        return GameProcessError(f"Unable to attach to process ID: {pid}")

    @staticmethod
    def create_config_error(key: str) -> ConfigValidationError:
        return ConfigValidationError(f"Missing required configuration key: {key}")