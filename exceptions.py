"""Custom exception classes for gaming automation handling edge cases."""


class GamingAutomationError(Exception):
    """Base exception for all gaming automation tool errors."""

    pass


class ProcessNotFoundError(GamingAutomationError):
    """Raised when the target game process cannot be located or hooked."""

    def __init__(self, process_name: str):
        self.process_name = process_name
        super().__init__(f"Game process '{process_name}' not found or inaccessible.")


class VisionDetectionError(GamingAutomationError):
    """Raised when template matching or visual recognition fails on game UI."""

    def __init__(self, element_name: str, confidence: float, threshold: float):
        self.element_name = element_name
        self.confidence = confidence
        self.threshold = threshold
        super().__init__(
            f"Failed to detect HUD element '{element_name}' "
            f"(confidence {confidence:.2f} < threshold {threshold:.2f})."
        )


class AntiCheatSafetyTriggered(GamingAutomationError):
    """Raised when anomalous delays or heuristic flags demand immediate abort."""

    def __init__(self, reason: str = "Suspicious input rate detected"):
        self.reason = reason
        super().__init__(f"Safety emergency stop triggered: {reason}")


class SequenceTimeoutError(GamingAutomationError):
    """Raised when an automated macro/action stalls beyond allowed time."""

    def __init__(self, sequence_id: str, elapsed: float, max_allowed: float):
        self.sequence_id = sequence_id
        self.elapsed = elapsed
        self.max_allowed = max_allowed
        super().__init__(
            f"Sequence '{sequence_id}' timed out after {elapsed:.1f}s "
            f"(limit: {max_allowed:.1f}s)."
        )
