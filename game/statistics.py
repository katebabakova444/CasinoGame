from collections import Counter
from game.game import Game

class Statistics:
    def analyze_basic(self, outcomes):
        counts = Counter(outcomes)
        wins = counts.get("win", 0)
        losses = counts.get("lose", 0)

        total_games = wins + losses
        win_rate = wins / total_games if total_games > 0 else 0

        return {
            "total_games": total_games,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate

        }
