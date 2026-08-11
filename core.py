from typing import List, Dict, Any

class Game:
    """
    Represents a game instance with attributes like title, genre, and player count.
    """
    def __init__(self, title: str, genre: str, player_count: int) -> None:
        self.title = title
        self.genre = genre
        self.player_count = player_count

    def get_info(self) -> Dict[str, Any]:
        """
        Returns a dictionary with game information.
        """
        return {
            'title': self.title,
            'genre': self.genre,
            'player_count': self.player_count
        }

class GameLibrary:
    """
    Manages a collection of games.
    """
    def __init__(self) -> None:
        self.games: List[Game] = []

    def add_game(self, game: Game) -> None:
        """
        Adds a game to the library.
        """
        self.games.append(game)

    def get_all_games(self) -> List[Dict[str, Any]]:
        """
        Returns a list of all games in the library as dictionaries.
        """
        return [game.get_info() for game in self.games]

if __name__ == '__main__':
    library = GameLibrary()
    library.add_game(Game('The Legend of Zelda', 'Action-Adventure', 1))
    library.add_game(Game('Fortnite', 'Battle Royale', 100))
    print(library.get_all_games())