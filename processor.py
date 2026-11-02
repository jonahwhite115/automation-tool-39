from typing import Dict, List, Any


def calculate_kda(kills: int, deaths: int, assists: int) -> float:
    """Calculate Kill/Death/Assist ratio with zero-death protection."""
    effective_deaths = max(1, deaths)
    return round((kills + assists) / effective_deaths, 2)


def process_match_stats(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process raw match telemetry payload into structured summary statistics.
    Useful for gaming bots, scrapers, and dashboard analytics.
    """
    player_name = raw_data.get("player_name", "Unknown")
    duration_seconds = raw_data.get("duration", 0)
    duration_minutes = max(1.0, duration_seconds / 60.0)

    kills = raw_data.get("kills", 0)
    deaths = raw_data.get("deaths", 0)
    assists = raw_data.get("assists", 0)
    score = raw_data.get("score", 0)

    kda = calculate_kda(kills, deaths, assists)
    score_per_minute = round(score / duration_minutes, 1)

    team_kills = raw_data.get("team_kills", 0)
    kill_participation = 0.0
    if team_kills > 0:
        kill_participation = round(((kills + assists) / team_kills) * 100, 1)

    return {
        "player_name": player_name,
        "match_id": raw_data.get("match_id", ""),
        "kda": kda,
        "score_per_minute": score_per_minute,
        "kill_participation_pct": kill_participation,
        "victory": raw_data.get("result") == "VICTORY",
        "processed_timestamp": raw_data.get("timestamp")
    }


def aggregate_session_stats(match_summaries: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Aggregate a list of processed match summaries for session tracking."""
    if not match_summaries:
        return {"matches_played": 0, "win_rate_pct": 0.0, "avg_kda": 0.0}

    total_matches = len(match_summaries)
    wins = sum(1 for m in match_summaries if m.get("victory", False))
    total_kda = sum(m.get("kda", 0.0) for m in match_summaries)

    return {
        "matches_played": total_matches,
        "wins": wins,
        "losses": total_matches - wins,
        "win_rate_pct": round((wins / total_matches) * 100, 1),
        "avg_kda": round(total_kda / total_matches, 2)
    }
