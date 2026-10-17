from typing import List, Dict, Optional

def calculate_win_rate(wins: int, total_games: int) -> float:
    """Calculates win percentage based on match history."""
    if total_games == 0:
        return 0.0
    return round((wins / total_games) * 100, 2)

def format_player_stats(player_name: str, stats: Dict[str, int]) -> str:
    """Converts player stats dictionary into a display-ready string."""
    level = stats.get("level", 1)
    xp = stats.get("xp", 0)
    return f"Player {player_name}: Lvl {level} ({xp} XP)"

def filter_active_sessions(sessions: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """Returns only active sessions from a provided list."""
    return [s for s in sessions if s.get("is_active", False)]

def validate_game_config(config: Dict[str, str]) -> bool:
    """Ensures all mandatory keys exist in the configuration."""
    required = ["server_id", "region", "version"]
    return all(key in config for key in required)

def get_session_latency(latency_data: List[int]) -> Optional[float]:
    """Computes average latency from a list of measurements."""
    if not latency_data:
        return None
    return sum(latency_data) / len(latency_data)