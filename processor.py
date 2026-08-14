import random
import time
from validators import validate_input

class GameProcessor:
    def __init__(self):
        self.running = True

    def start(self):
        while self.running:
            user_input = input("Enter your command: ")
            if self.process_input(user_input):
                print("Processed successfully.")
            else:
                print("Invalid command, please try again.")

    def process_input(self, user_input):
        if validate_input(user_input):
            # Simulated processing logic
            print(f"Processing command: {user_input}")
            time.sleep(random.uniform(0.5, 1.5))  # Simulating processing time
            return True
        return False

if __name__ == '__main__':
    game_processor = GameProcessor()
    game_processor.start()