from typing import Union, List

def validate_game_config(config: dict) -> bool:
    """
    Validate that the gaming configuration contains essential keys.

    Args:
        config: A dictionary containing game settings.

    Returns:
        True if valid, False otherwise.
    """
    required_keys: List[str] = ['game_id', 'resolution', 'fps_limit']
    return all(key in config for key in required_keys)

def sanitize_input(value: Union[str, int]) -> str:
    """
    Clean user input to prevent injection in gaming commands.

    Args:
        value: The raw input string or integer.

    Returns:
        A sanitized string representation.
    """
    if isinstance(value, int):
        return str(value)
    return str(value).strip().replace(';', '')

def check_port_range(port: int) -> bool:
    """
    Verify if the network port is within the gaming range.

    Args:
        port: Integer port number to check.

    Returns:
        Boolean status of port availability.
    """
    return 1024 <= port <= 65535