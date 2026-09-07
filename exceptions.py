"""Custom exceptions for gaming data handling and automation pipeline."""

from typing import Any, Dict, Optional


class GamingDataError(Exception):
    """Base exception for all gaming data processing errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} | Context: {self.details}"
        return self.message


class TelemetryParsingError(GamingDataError):
    """Raised when raw game telemetry payload cannot be parsed."""

    def __init__(self, raw_payload: str, reason: str) -> None:
        message = f"Failed to parse telemetry data: {reason}"
        details = {"payload_sample": raw_payload[:100]}
        super().__init__(message, details)


class InvalidPlayerDataError(GamingDataError):
    """Raised when player profile or inventory stats fail validation."""

    def __init__(self, player_id: str, field_name: str, expected_type: str) -> None:
        message = f"Invalid player data attribute '{field_name}'"
        details = {
            "player_id": player_id,
            "field": field_name,
            "expected_type": expected_type,
        }
        super().__init__(message, details)


class MatchDataNotFoundError(GamingDataError):
    """Raised when requested match or lobby ID is missing from API data."""

    def __init__(self, match_id: str) -> None:
        message = f"Match record for ID '{match_id}' not found"
        details = {"match_id": match_id}
        super().__init__(message, details)
