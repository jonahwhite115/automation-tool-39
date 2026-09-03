"""Validation utilities for gaming automation inputs and game state parameters."""

from typing import Tuple, Union


def validate_coordinates(coords: Tuple[int, int], max_bounds: Tuple[int, int]) -> bool:
    """Validate if screen coordinates fall within acceptable screen dimensions.

    Args:
        coords: A tuple of (x, y) pixel coordinates.
        max_bounds: A tuple of (max_width, max_height) screen resolution.

    Returns:
        True if coordinates are non-negative and within bounds, False otherwise.
    """
    x, y = coords
    max_x, max_y = max_bounds
    return 0 <= x < max_x and 0 <= y < max_y


def validate_health_percentage(hp: Union[int, float]) -> float:
    """Ensure health percentage value is clamped between 0.0 and 100.0.

    Args:
        hp: The raw health percentage value to validate.

    Returns:
        A float value strictly between 0.0 and 100.0.

    Raises:
        TypeError: If hp is not a numeric type.
        ValueError: If hp is less than zero.
    """
    if not isinstance(hp, (int, float)):
        raise TypeError("Health value must be a numeric type.")
    
    val = float(hp)
    if val < 0.0:
        raise ValueError("Health percentage cannot be negative.")
    
    return min(100.0, max(0.0, val))


def validate_inventory_slot(slot_index: int, total_slots: int = 36) -> bool:
    """Check if an inventory slot index is valid for the current grid size.

    Args:
        slot_index: Zero-based inventory slot index.
        total_slots: Maximum available slots in inventory (default 36).

    Returns:
        True if slot_index is valid, False otherwise.
    """
    return 0 <= slot_index < total_slots
