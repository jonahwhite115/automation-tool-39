from typing import List, Optional, Union

def validate_game_config(config: dict) -> bool:
    """
    Validates the mandatory configuration fields for the gaming automation tool.

    Args:
        config: A dictionary containing game settings like paths and resolutions.

    Returns:
        True if the configuration is valid, False otherwise.
    """
    required_keys: List[str] = ["game_path", "resolution", "fps_limit"]
    return all(key in config for key in required_keys)

def sanitize_input(value: Union[str, int]) -> str:
    """
    Cleans and prepares input strings for the automation engine.

    Args:
        value: The raw input value from the user or configuration file.

    Returns:
        A stripped and lowercase version of the input string.
    """
    return str(value).strip().lower()

def check_threshold(value: float, min_val: float, max_val: Optional[float] = None) -> bool:
    """
    Checks if a numeric metric falls within an allowed gaming range.

    Args:
        value: The current metric to validate.
        min_val: The minimum allowed threshold.
        max_val: The maximum allowed threshold (optional).

    Returns:
        True if value is within bounds, False otherwise.
    """
    if max_val is not None:
        return min_val <= value <= max_val
    return value >= min_val