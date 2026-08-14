def validate_username(username):
    if not isinstance(username, str):
        return False, 'Username must be a string'
    if len(username) < 3 or len(username) > 20:
        return False, 'Username must be between 3 and 20 characters'
    if not username.isalnum():
        return False, 'Username must be alphanumeric'
    return True, 'Valid username'


def validate_score(score):
    if not isinstance(score, int):
        return False, 'Score must be an integer'
    if score < 0:
        return False, 'Score cannot be negative'
    return True, 'Valid score'


def validate_choice(choice, valid_choices):
    if choice not in valid_choices:
        return False, f'Choice must be one of {valid_choices}'
    return True, 'Valid choice'


# Example usage within a main processing loop
if __name__ == '__main__':
    user = input('Enter your username: ')
    valid, message = validate_username(user)
    if not valid:
        print(message)
    else:
        # Continue processing with valid username
        score = int(input('Enter your score: '))
        valid, message = validate_score(score)
        if not valid:
            print(message)
        else:
            choice = input('Make a choice (a/b/c): ')
            valid, message = validate_choice(choice, ['a', 'b', 'c'])
            if not valid:
                print(message)
            else:
                # Proceed with game logic
                print('Game logic proceeds here...')
