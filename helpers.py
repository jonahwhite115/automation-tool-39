import random
import string

class GameHelper:
    @staticmethod
    def generate_random_string(length=10):
        """Generate a random string of fixed length."""
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    @staticmethod
    def get_user_input(prompt):
        """Get input from the user with a prompt."""
        return input(prompt)

    @staticmethod
    def display_message(message):
        """Display a message to the user."""
        print(message)

    @staticmethod
    def validate_choice(choice, valid_choices):
        """Validate if the user choice is within valid options."""
        return choice in valid_choices

    @staticmethod
    def clear_console():
        """Clear the console screen for better readability."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

# Example Usage in a game
if __name__ == '__main__':
    GameHelper.clear_console()
    name = GameHelper.get_user_input('Enter your name: ')
    GameHelper.display_message(f'Welcome to the game, {name}!')
    GameHelper.display_message('Your random code is: ' + GameHelper.generate_random_string(8))
