import time

class GameProcessor:
    def __init__(self):
        self.games = []
        self.execution_times = []

    def add_game(self, game):
        self.games.append(game)

    def process_games(self):
        start = time.perf_counter()
        for game in self.games:
            self.process_single_game(game)
        end = time.perf_counter()
        print(f'Processed {len(self.games)} games in {end - start:.4f} seconds')

    def process_single_game(self, game):
        # Example processing logic
        time.sleep(0.1)  # Simulate a time-consuming operation

    def optimize_processing(self):
        if len(self.games) > 5:
            self.games = self.games[:5]  # Limit to first 5 games
        self.process_games()