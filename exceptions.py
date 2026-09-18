class AutomationError(Exception):
    """Base exception class for automation-tool-39."""
    pass

class PerformanceLimitExceeded(AutomationError):
    """Raised when game state updates exceed frequency thresholds."""
    def __init__(self, message="Update frequency limit exceeded", threshold=0.01):
        self.threshold = threshold
        super().__init__(f"{message}: {threshold}s interval required")

class ResourceConstraintError(AutomationError):
    """Raised when system memory or CPU spikes occur."""
    pass

class ConnectionTimeoutError(AutomationError):
    """Raised during unstable game process communication."""
    pass

def validate_timing(interval: float, threshold: float = 0.01):
    """Utility to enforce strict execution frequency constraints."""
    if interval < threshold:
        raise PerformanceLimitExceeded(threshold=threshold)
    return True