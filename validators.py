import logging

def validate_game_input(user_input: str) -> bool:
    """
    Validates player commands to prevent malformed data injection.
    Ensures inputs are within expected length and character sets.
    """
    MAX_INPUT_LENGTH = 32
    ALLOWED_CHARACTERS = set('abcdefghijklmnopqrstuvwxyz0123456789_ ')

    if not isinstance(user_input, str):
        logging.error("Input must be a string.")
        return False

    if len(user_input) == 0 or len(user_input) > MAX_INPUT_LENGTH:
        logging.warning(f"Input length {len(user_input)} is invalid.")
        return False

    if not all(c in ALLOWED_CHARACTERS for c in user_input.lower()):
        logging.warning("Input contains forbidden characters.")
        return False

    return True

def process_game_command(raw_input: str):
    """
    Main loop processor entry point for validated commands.
    """
    if validate_game_input(raw_input):
        return f"Executing: {raw_input}"
    else:
        return "Error: invalid input received"
