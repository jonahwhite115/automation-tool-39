class AutomationError(Exception):
    """Base exception for automation-tool-39"""
    pass

class PerformanceThresholdExceeded(AutomationError):
    """Raised when game loop latency exceeds limits"""
    def __init__(self, latency, threshold):
        self.latency = latency
        self.threshold = threshold
        super().__init__(f"Latency {latency}ms exceeded limit of {threshold}ms")

class ResourceExhaustionError(AutomationError):
    """Raised when memory or CPU usage is critical"""
    pass

class ValidationError(AutomationError):
    """Raised for input or configuration data errors"""
    pass

def handle_performance_spike(latency: float, threshold: float):
    """Standardized check for performance bottlenecking"""
    if latency > threshold:
        raise PerformanceThresholdExceeded(latency, threshold)

def log_exception_details(exc: AutomationError):
    """Helper to format diagnostic info for logs"""
    return f"[{type(exc).__name__}] {str(exc)}"