"""Custom exceptions for handling gaming automation edge cases."""

class AutomationError(Exception):
    """Base exception for all gaming automation errors."""
    def __init__(self, message: str, details: dict = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} | Details: {self.details}"
        return self.message


class GameWindowNotFoundError(AutomationError):
    """Raised when the target game process or window cannot be located."""
    def __init__(self, window_title: str):
        super().__init__(
            f"Target game window '{window_title}' was not found",
            {"window_title": window_title}
        )


class TemplateMatchingError(AutomationError):
    """Raised when a game UI element or screen template fails to match."""
    def __init__(self, template_name: str, confidence: float, threshold: float):
        super().__init__(
            f"UI template '{template_name}' match failed: confidence {confidence:.2f} below threshold {threshold:.2f}",
            {"template": template_name, "confidence": confidence, "threshold": threshold}
        )


class ActionTimeoutError(AutomationError):
    """Raised when waiting for a game state transition exceeds time limit."""
    def __init__(self, expected_state: str, timeout_seconds: float):
        super().__init__(
            f"Timed out waiting for game state '{expected_state}' after {timeout_seconds}s",
            {"expected_state": expected_state, "timeout_seconds": timeout_seconds}
        )


class SafetySafetyInterruptedError(AutomationError):
    """Raised when automated input is interrupted by unexpected window focus or anti-bot check."""
    def __init__(self, reason: str):
        super().__init__(
            f"Automation safety abort triggered: {reason}",
            {"reason": reason}
        )
