from typing import List, Dict, Optional

class GameAutomationEngine:
    """Core engine for handling game automation routines."""

    def __init__(self, target_window: str, delay: float = 0.5) -> None:
        self.target_window: str = target_window
        self.delay: float = delay
        self.state: Dict[str, bool] = {"running": False}

    def get_game_state(self) -> Dict[str, bool]:
        """Retrieve the current status of the game session."""
        return self.state

    def execute_macro(self, sequence: List[str]) -> bool:
        """Execute a list of predefined input commands."""
        if not sequence:
            return False
        
        print(f"Executing {len(sequence)} commands on {self.target_window}")
        self.state["running"] = True
        return True

    def update_config(self, key: str, value: Optional[float] = None) -> None:
        """Update engine operational parameters."""
        if value is not None:
            setattr(self, key, value)

def initialize_session(window_name: str) -> GameAutomationEngine:
    """Factory function to spawn an engine instance."""
    return GameAutomationEngine(target_window=window_name)