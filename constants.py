import os

# Configuration constants for automation-tool-39
# Defines system boundaries and validation rules

MAX_RETRY_ATTEMPTS = 5
TIMEOUT_SECONDS = 30.0

# Supported gaming platforms for automation tasks
SUPPORTED_PLATFORMS = {
    "steam",
    "epic",
    "gog",
    "origin"
}

# Validation ranges for input automation scripts
MIN_DELAY_MS = 100
MAX_DELAY_MS = 5000

# Environment path defaults with fallback logic
BASE_PATH = os.getenv("AUTO_TOOL_PATH", "./data")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

# Error message constants for consistent exception reporting
ERR_INVALID_PLATFORM = "Target platform not supported for automation."
ERR_TIMEOUT_REACHED = "Operation timed out after maximum retry attempts."
ERR_PATH_NOT_FOUND = "Configuration or data path could not be resolved."

class ConstantsError(Exception):
    """Custom base exception for constant configuration errors."""
    pass

def get_validated_delay(delay: int) -> int:
    """Ensures delay falls within operational safety bounds."""
    if not isinstance(delay, int):
        raise ConstantsError("Delay must be an integer.")
    return max(MIN_DELAY_MS, min(delay, MAX_DELAY_MS))
