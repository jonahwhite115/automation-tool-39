import json
import logging

class GameHandler:
    def __init__(self):
        self.games = []
        logging.basicConfig(level=logging.INFO)

    def add_game(self, game):
        if not isinstance(game, dict):
            logging.error('Game must be a dictionary')
            raise ValueError('Game must be a dictionary')
        if 'name' not in game or 'genre' not in game:
            logging.error('Game must contain name and genre')
            raise KeyError('Game must contain name and genre')
        self.games.append(game)
        logging.info(f'Game added: {game}\n')

    def get_game(self, name):
        try:
            return next(g for g in self.games if g['name'] == name)
        except StopIteration:
            logging.error(f'Game not found: {name}')
            return None

    def list_games(self):
        if not self.games:
            logging.warning('No games available')
            return 'No games available'
        return json.dumps(self.games, indent=4)

    def remove_game(self, name):
        for i, game in enumerate(self.games):
            if game['name'] == name:
                del self.games[i]
                logging.info(f'Game removed: {name}')
                return
        logging.error(f'Game not found for removal: {name}')
        raise ValueError('Game not found')

# Example Usage (uncomment for testing)
# if __name__ == '__main__':
#     handler = GameHandler()
#     handler.add_game({'name': 'Cyberpunk 2077', 'genre': 'RPG'})
#     print(handler.list_games())
#     print(handler.get_game('Cyberpunk 2077'))
#     handler.remove_game('Cyberpunk 2077')
#     print(handler.list_games())