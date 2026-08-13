import random
import sys

class Game:
    def __init__(self):
        self.score = 0
        self.max_score = 100
        self.input_choices = ['a', 'b', 'c']

    def validate_input(self, user_input):
        if user_input not in self.input_choices:
            raise ValueError(f"Invalid choice: {user_input}. Please choose from {self.input_choices}.")

    def play(self):
        print("Welcome to the game!")
        while self.score < self.max_score:
            user_input = input(f"Current score: {self.score}. Choose 'a', 'b', or 'c': ")
            try:
                self.validate_input(user_input)
                self.update_score(user_input)
            except ValueError as e:
                print(e)

        print("Congratulations! You've reached the maximum score!")

    def update_score(self, choice):
        self.score += random.randint(1, 10)  # Simulate scoring

if __name__ == '__main__':
    game = Game()
    game.play()