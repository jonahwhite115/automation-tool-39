from typing import Final, Dict, List

# Configuration for gaming telemetry
DEFAULT_POLL_RATE: Final[float] = 0.5
MAX_RETRY_ATTEMPTS: Final[int] = 3

# Standardized player status codes
STATUS_CODES: Final[Dict[int, str]] = {
    0: "OFFLINE",
    1: "IN_LOBBY",
    2: "IN_GAME",
    3: "MATCHMAKING"
}

# Validation constraints for game assets
SUPPORTED_PLATFORMS: Final[List[str]] = ["pc", "ps5", "xbox", "switch"]
ASSET_TIMEOUT_SECONDS: Final[int] = 30

# Logging categories for automation tool
LOG_CATEGORIES: Final[List[str]] = [
    "NETWORK",
    "ASSET_SYNC",
    "PLAYER_STATE",
    "ERROR_HANDLING"
]

def get_status_label(code: int) -> str:
    """Retrieve human-readable status from integer code."""
    return STATUS_CODES.get(code, "UNKNOWN")

if __name__ == "__main__":
    # Verification of constants integration
    print(f"Active platforms: {', '.join(SUPPORTED_PLATFORMS)}")