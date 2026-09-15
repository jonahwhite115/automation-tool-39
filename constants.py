import math
from typing import Final

# performance-critical gaming engine constants
# caching computed values to prevent redundant overhead

POLLING_RATE_HZ: Final[int] = 120
FRAME_TIME_MS: Final[float] = 1000.0 / POLLING_RATE_HZ

# optimized math constants for high-frequency coordinate geometry
SQRT_2: Final[float] = math.sqrt(2)
PI_DIV_180: Final[float] = math.pi / 180.0

# buffer limits for memory-efficient automation processing
MAX_INPUT_QUEUE_SIZE: Final[int] = 1024
CACHE_EXPIRY_SECONDS: Final[int] = 30

# network latency threshold constants
LATENCY_THRESHOLD_MS: Final[int] = 50
RETRY_DELAY_SECONDS: Final[float] = 0.5

# coordinate space bounds for viewport scaling calculations
VIEWPORT_WIDTH: Final[int] = 1920
VIEWPORT_HEIGHT: Final[int] = 1080

# performance bitmasks for event filtering
EVENT_TYPE_INPUT: Final[int] = 0b0001
EVENT_TYPE_NETWORK: Final[int] = 0b0010
EVENT_TYPE_RENDER: Final[int] = 0b0100