class AutomationError(Exception):
    """Base exception for all gaming automation errors."""
    pass


class GameClientError(AutomationError):
    """Raised when the game client is not running or fails to respond."""

    def __init__(self, message: str = "Game client is not running or unreachable"):
        super().__init__(message)


class DetectionError(AutomationError):
    """Raised when image search or pixel detection fails on screen."""

    def __init__(self, target_name: str, message: str = None):
        self.target_name = target_name
        msg = message or f"Failed to detect visual element: '{target_name}'"
        super().__init__(msg)


class ActionTimeoutError(AutomationError):
    """Raised when an automation macro or action exceeds its allotted time."""

    def __init__(self, action_name: str, timeout_seconds: float):
        self.action_name = action_name
        self.timeout_seconds = timeout_seconds
        super().__init__(
            f"Action '{action_name}' timed out after {timeout_seconds}s"
        )


class InputBlockedError(AutomationError):
    """Raised when simulated inputs are blocked by anti-cheat or system permissions."""

    def __init__(
        self, message: str = "Input simulation blocked by the target game window"
    ):
        super().__init__(message)
