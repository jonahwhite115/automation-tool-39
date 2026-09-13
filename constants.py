import os
from typing import Final

# performance constants for core game engine loops
CACHE_SIZE: Final[int] = 1024
CHUNK_SIZE: Final[int] = 4096
MAX_THREADS: Final[int] = os.cpu_count() or 4

# memory optimization thresholds
BUFFER_THRESHOLD: Final[float] = 0.85
GC_COLLECTION_INTERVAL: Final[int] = 300

# network polling frequency in seconds
POLL_RATE: Final[float] = 0.016

# shared resource locks status
USE_FAST_LOCKS: Final[bool] = True

def get_optimization_mode() -> str:
    """returns current performance configuration profile"""
    return "high_performance" if MAX_THREADS > 4 else "balanced"

# global registry for entity component processing
ENTITY_COMPONENT_TYPES = [
    "position",
    "velocity",
    "render",
    "collision",
    "input"
]