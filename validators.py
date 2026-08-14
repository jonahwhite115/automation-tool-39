def validate_input(user_input):
    """
    Validates user input to ensure it is within expected parameters.
    :param user_input: The input from the user.
    :return: True if input is valid, False otherwise.
    """
    if not isinstance(user_input, str):
        return False
    if len(user_input) < 1:
        return False
    return True

if __name__ == '__main__':
    while True:
        user_input = input('Enter your command: ')
        if validate_input(user_input):
            print(f'Valid input: {user_input}')
            # Proceed with processing the command
        else:
            print('Invalid input. Please try again.')