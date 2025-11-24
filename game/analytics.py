from game.game import Game
from collections import Counter

class GameAnalytics:
    def analyze_rolls(self, game, history, roll_groups):
        counts_history = Counter(history)
        most_common_roll = counts_history.most_common(1)

        win_counts = Counter(roll_groups["win"])
        lose_counts = Counter(roll_groups["lose"])

        most_common_win_roll = win_counts.most_common(1)
        most_common_lose_roll = lose_counts.most_common(1)

        total_games = len(history)
        profit = game.balance - game.start_balance
        if total_games > 0:
            avg_profit = profit / total_games
        else:
            avg_profit = 0

        return {
            "most_common_roll": most_common_roll,
            "most_common_win_roll": most_common_win_roll,
            "most_common_lose_roll": most_common_lose_roll,
            "average_profit_per_game": avg_profit
        }



