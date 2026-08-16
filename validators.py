def validate_player_name(name):
    if not isinstance(name, str):
        raise ValueError('Player name must be a string')
    if len(name) < 1 or len(name) > 20:
        raise ValueError('Player name must be between 1 and 20 characters')
    return True


def validate_score(score):
    if not isinstance(score, (int, float)):
        raise ValueError('Score must be an integer or float')
    if score < 0:
        raise ValueError('Score must be non-negative')
    return True


def validate_level(level):
    if not isinstance(level, int):
        raise ValueError('Level must be an integer')
    if level < 1 or level > 100:
        raise ValueError('Level must be between 1 and 100')
    return True


def validate_game_input(player_name, score, level):
    validate_player_name(player_name)
    validate_score(score)
    validate_level(level)
    return True
