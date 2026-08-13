import json

class GameInput:
    def __init__(self):
        self.valid_actions = ['move', 'attack', 'defend', 'heal']

    def validate_action(self, action):
        if action not in self.valid_actions:
            raise ValueError(f'Invalid action: {action}')

def main_loop():
    game_input = GameInput()
    while True:
        user_input = input('Enter your action: ')
        try:
            game_input.validate_action(user_input)
            print(f'Action {user_input} executed.')
        except ValueError as e:
            print(e)
            print('Please choose a valid action from the list: move, attack, defend, heal.')

if __name__ == '__main__':
    main_loop()