class GameManager:
    def __init__(self):
        self.players = []

    def add_player(self, player_name):
        self.players.append(player_name)

    def remove_player(self, player_name):
        self.players.remove(player_name)

    def get_player_count(self):
        return len(self.players)

    def start_game(self):
        if len(self.players) < 2:
            raise ValueError("Not enough players to start the game.")
        print("Game started with players:", self.players)

    def optimize_performance(self):
        # Removing duplicates to optimize space
        self.players = list(set(self.players))

    def reset_game(self):
        self.players.clear()
        print("Game reset, players cleared.")

if __name__ == '__main__':
    game_manager = GameManager()
    game_manager.add_player('Alice')
    game_manager.add_player('Bob')
    game_manager.optimize_performance()
    print("Current player count:", game_manager.get_player_count())
    game_manager.start_game()
    game_manager.reset_game()