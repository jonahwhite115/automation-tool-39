import random
import logging

class GameError(Exception):
    pass

class GameHandler:
    def __init__(self):
        self.score = 0
        logging.basicConfig(level=logging.INFO)

    def play(self):
        try:
            result = self.perform_action()
            logging.info(f'Action result: {result}')
        except GameError as e:
            logging.error(f'Game error occurred: {str(e)}')
        except Exception as e:
            logging.exception('An unexpected error occurred')

    def perform_action(self):
        action = random.choice(['win', 'lose', 'error'])
        if action == 'error':
            raise GameError('Simulated error during action')
        elif action == 'win':
            self.score += 10
            return 'You won!'
        else:
            self.score -= 5
            return 'You lost!'

if __name__ == '__main__':
    handler = GameHandler()
    handler.play()
    logging.info(f'Final score: {handler.score}')