import os

# Configuration constants for automation-tool-39
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# Gaming environment paths
GAME_EXECUTABLE_PATH = os.getenv("GAME_PATH", "/usr/local/bin/game")
CONFIG_FILE = "config.json"

# Error message mapping for edge cases
ERROR_MESSAGES = {
    "MISSING_FILE": "The required game configuration file was not found.",
    "TIMEOUT_EXCEEDED": "The game process failed to respond within limits.",
    "INVALID_STATE": "An illegal state transition was detected in the game loop.",
    "PERMISSION_DENIED": "Insufficient system privileges to modify game memory.",
    "PROCESS_NOT_RUNNING": "Target game process is not currently active."
}

# Supported resolutions for display parsing
SUPPORTED_RESOLUTIONS = [
    (1920, 1080),
    (2560, 1440),
    (3840, 2160)
]

# Network constraints
MAX_LATENCY_MS = 150
CONNECTION_RETRY_DELAY = 5

def get_error_message(code: str) -> str:
    """Retrieve standardized error message or fallback string."""
    return ERROR_MESSAGES.get(code, "An unknown internal error occurred.")