def validate_player_score(score):
    """
    Validates the player's score.
    Raises ValueError if the score is invalid.
    """
    if not isinstance(score, (int, float)):
        raise ValueError('Score must be a number.')
    if score < 0:
        raise ValueError('Score cannot be negative.')
    return True


def validate_game_state(state):
    """
    Validates the current game state.
    Raises ValueError if the state is not valid.
    """
    valid_states = ['ongoing', 'paused', 'finished']
    if state not in valid_states:
        raise ValueError(f'State must be one of {valid_states}.')
    return True


def validate_player_action(action):
    """
    Validates the player's action.
    Raises ValueError if the action is not valid.
    """
    valid_actions = ['move', 'attack', 'defend']
    if action not in valid_actions:
        raise ValueError(f'Action must be one of {valid_actions}.')
    return True

