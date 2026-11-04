import logging
from typing import Tuple, Any

logger = logging.getLogger(__name__)

class ScreenBoundsError(ValueError):
    """Raised when screen coordinates or dimensions fall outside valid boundaries."""
    pass

def scale_bounding_box(
    box: Tuple[int, int, int, int],
    base_resolution: Tuple[int, int],
    target_resolution: Tuple[int, int]
) -> Tuple[int, int, int, int]:
    """Scales UI bounding box (x, y, width, height) between display resolutions.

    Handles edge cases such as zero/negative resolution dimensions and out-of-bounds coordinates.
    """
    base_w, base_h = base_resolution
    target_w, target_h = target_resolution

    # Edge case: Invalid screen dimensions
    if base_w <= 0 or base_h <= 0 or target_w <= 0 or target_h <= 0:
        logger.error(f"Invalid resolutions provided: base={base_resolution}, target={target_resolution}")
        raise ScreenBoundsError("Resolution dimensions must be strictly positive integers.")

    x, y, w, h = box

    # Edge case: Negative dimensions or out-of-range coordinates
    if w < 0 or h < 0:
        logger.warning(f"Negative width/height detected in box {box}. Standardizing to zero.")
        w = max(0, w)
        h = max(0, h)

    try:
        scale_x = target_w / float(base_w)
        scale_y = target_h / float(base_h)

        scaled_x = int(round(x * scale_x))
        scaled_y = int(round(y * scale_y))
        scaled_w = int(round(w * scale_x))
        scaled_h = int(round(h * scale_y))

        # Clamp coordinates within target display boundaries
        clamped_x = max(0, min(scaled_x, target_w))
        clamped_y = max(0, min(scaled_y, target_h))
        clamped_w = min(scaled_w, max(0, target_w - clamped_x))
        clamped_h = min(scaled_h, max(0, target_h - clamped_y))

        return (clamped_x, clamped_y, clamped_w, clamped_h)

    except ZeroDivisionError as e:
        logger.critical("Unexpected zero division during coordinate scaling calculation.")
        raise ScreenBoundsError("Resolution scaling failed due to zero dimension.") from e
    except Exception as e:
        logger.exception("Unexpected error occurred while scaling bounding box.")
        raise ScreenBoundsError(f"Failed to scale bounding box {box}: {e}") from e

def safe_parse_game_metric(raw_val: Any, default: float = 0.0) -> float:
    """Safely parses raw game telemetry metrics (e.g., health, mana) handling corrupt data types."""
    if raw_val is None:
        return default

    try:
        val = float(raw_val)
        # Edge case: NaN or Infinity values from corrupt memory reads
        if val != val or val in (float('inf'), float('-inf')):
            logger.warning(f"Non-finite metric value encountered: {raw_val}, falling back to default.")
            return default
        return val
    except (ValueError, TypeError):
        logger.warning(f"Corrupt game metric value: {raw_val}, using default {default}.")
        return default
