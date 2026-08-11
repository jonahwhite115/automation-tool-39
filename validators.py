import re

def validate_username(username):
    """
    Validates the provided username.
    Conditions:
    - Must be alphanumeric
    - Length should be between 3 and 15 characters
    """
    if not re.match('^[A-Za-z0-9]{3,15}$', username):
        raise ValueError('Username must be 3-15 characters long and alphanumeric.')


def validate_score(score):
    """
    Validates the provided score.
    Conditions:
    - Must be a non-negative integer
    """
    if not isinstance(score, int) or score < 0:
        raise ValueError('Score must be a non-negative integer.')


def validate_game_input(username, score):
    """
    Validates both username and score before processing the game.
    """
    validate_username(username)
    validate_score(score)

if __name__ == '__main__':
    # Example of validation usage
    try:
        validate_game_input('Player1', 100)
        print('Input is valid!')
    except ValueError as e:
        print(f'Validation error: {e}')