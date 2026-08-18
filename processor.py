from typing import List, Dict

class GameProcessor:
    """ A class to process game data for analysis and reporting. """

    def __init__(self, game_data: List[Dict]) -> None:
        """ Initializes the GameProcessor with game data. """
        self.game_data = game_data

    def filter_by_score(self, min_score: int) -> List[Dict]:
        """ Filters the game data by a minimum score. """ 
        return [game for game in self.game_data if game.get('score', 0) >= min_score]

    def get_average_score(self) -> float:
        """ Calculates the average score of the games. """ 
        total_score = sum(game.get('score', 0) for game in self.game_data)
        return total_score / len(self.game_data) if self.game_data else 0.0

    def top_n_games(self, n: int) -> List[Dict]:
        """ Retrieves the top N games based on score. """ 
        return sorted(self.game_data, key=lambda x: x.get('score', 0), reverse=True)[:n]

# Example usage
if __name__ == '__main__':
    games = [
        {'name': 'Game A', 'score': 85},
        {'name': 'Game B', 'score': 92},
        {'name': 'Game C', 'score': 75},
    ]
    processor = GameProcessor(games)
    print(processor.get_average_score())  # Outputs average score
    print(processor.top_n_games(2))       # Outputs top 2 games
