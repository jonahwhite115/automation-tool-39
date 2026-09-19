from typing import Dict, List, Any, Optional

class MatchDataHandler:
    """Utility for processing and aggregating multiplayer game match data."""

    def __init__(self, match_id: str):
        self.match_id = match_id
        self.players: List[Dict[str, Any]] = []

    def add_player_performance(self, username: str, kills: int, deaths: int, assists: int, score: int) -> None:
        """Adds a player's statistics to the current match."""
        self.players.append({
            "username": username,
            "kills": max(0, kills),
            "deaths": max(0, deaths),
            "assists": max(0, assists),
            "score": max(0, score)
        })

    def calculate_kda(self, player_stats: Dict[str, Any]) -> float:
        """Calculates Kill-Death-Assist ratio with weighted assists."""
        deaths = player_stats["deaths"]
        if deaths == 0:
            return float(player_stats["kills"] + player_stats["assists"])
        return round((player_stats["kills"] + (player_stats["assists"] * 0.5)) / deaths, 2)

    def determine_mvp(self) -> Optional[str]:
        """Identifies the MVP based on kills, assists, score, and deaths."""
        if not self.players:
            return None

        best_performance = -1.0
        mvp_name = None

        for player in self.players:
            perf_score = (
                player["kills"] * 1.5 +
                player["assists"] * 0.75 +
                (player["score"] / 100.0) -
                (player["deaths"] * 0.5)
            )
            if perf_score > best_performance:
                best_performance = perf_score
                mvp_name = player["username"]

        return mvp_name

    def get_match_summary(self) -> Dict[str, Any]:
        """Returns aggregated statistics for the entire match."""
        if not self.players:
            return {"match_id": self.match_id, "total_players": 0, "mvp": None}

        total_kills = sum(p["kills"] for p in self.players)
        total_deaths = sum(p["deaths"] for p in self.players)
        mvp = self.determine_mvp()

        return {
            "match_id": self.match_id,
            "total_players": len(self.players),
            "total_kills": total_kills,
            "total_deaths": total_deaths,
            "mvp": mvp,
            "average_kda": round(sum(self.calculate_kda(p) for p in self.players) / len(self.players), 2)
        }