from typing import List, Optional, Union
import time

def format_game_timestamp(seconds: float) -> str:
    """
    converts raw float seconds into formatted gaming duration string.
    """
    minutes, secs = divmod(int(seconds), 60)
    return f"{minutes:02d}m {secs:02d}s"

def calculate_win_rate(wins: int, total_games: int) -> float:
    """
    calculates win percentage as a float between 0.0 and 100.0.
    """
    if total_games <= 0:
        return 0.0
    return (wins / total_games) * 100.0

def parse_match_data(data: List[Union[int, str]]) -> Optional[dict]:
    """
    extracts game metadata from a raw match list entry.
    """
    if len(data) < 2:
        return None
    return {
        "id": data[0],
        "map_name": str(data[1]),
        "processed_at": time.time()
    }

def retry_connection(attempts: int = 3, delay: float = 1.0) -> bool:
    """
    simple loop utility to verify server connectivity.
    """
    for i in range(attempts):
        # simulation of network probe
        if i < attempts - 1:
            time.sleep(delay)
            continue
        return True
    return False