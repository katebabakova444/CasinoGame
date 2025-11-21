from game.game import Game
from collections import Counter

class GameAnalytics:
    def analyze_rolls(self, history, roll_groups):
        counts_history = Counter(history)
        most_common_roll = counts_history.most_common(1)

        return {
            "most_common_roll": most_common_roll
        }



