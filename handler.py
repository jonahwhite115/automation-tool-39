from typing import List, Dict

class GameHandler:
    """Handles game logic and operations."""

    def __init__(self, game_name: str) -> None:
        """Initialize the game handler with a game name."""
        self.game_name = game_name
        self.players: List[str] = []

    def add_player(self, player_name: str) -> None:
        """Add a player to the game."""
        self.players.append(player_name)

    def remove_player(self, player_name: str) -> bool:
        """Remove a player from the game.

        Returns True if the player was removed, False otherwise."""
        try:
            self.players.remove(player_name)
            return True
        except ValueError:
            return False

    def get_players(self) -> List[str]:
        """Return the list of players currently in the game."""
        return self.players

    def start_game(self) -> None:
        """Start the game with the current players."""
        if len(self.players) < 2:
            raise ValueError("Not enough players to start the game.")
        print(f"{self.game_name} is starting with players: {', '.join(self.players)}")

    def reset_game(self) -> None:
        """Reset the game by clearing the player list."""
        self.players.clear()
        print(f"{self.game_name} has been reset.")
