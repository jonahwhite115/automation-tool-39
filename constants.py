import os

# Configuration constants for automation-tool-39
DEFAULT_RETRY_ATTEMPTS = 3
TIMEOUT_SECONDS = 30

# Gaming process monitoring limits
MAX_PROCESS_RESTARTS = 5
POLLING_INTERVAL = 0.5

# File system paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "logs", "automation.log")

# Error handling status codes
STATUS_OK = 0
STATUS_RETRYABLE_ERROR = 1
STATUS_FATAL_ERROR = 2

# Supported game engines
SUPPORTED_ENGINES = {"unreal", "unity", "custom"}

def get_timeout_value(env_var: str = "") -> int:
    """Fetches timeout from environment or returns default."""
    try:
        return int(os.environ.get(env_var, TIMEOUT_SECONDS))
    except (ValueError, TypeError):
        return TIMEOUT_SECONDS