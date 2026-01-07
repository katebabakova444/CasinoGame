from collections import Counter
from game.game import Game
class MonteCarloSimulator:
    def __init__(self, storage=None):
        self.storage = storage

    def run_simulation(self, runs, bet, rounds_per_run=1):
        total_wins = 0
        total_losses = 0
        profits = []
        win_rolls = Counter()
        lose_rolls = Counter()

        for i in range(runs):
            g = Game(balance=100, storage=self.storage)
            for r in range(rounds_per_run):
                result = g.play_round(bet)
                dice1, dice2 = result["dice"]

                if result["outcome"] == "win":
                    total_wins += 1
                    win_rolls[(dice1, dice2)] += 1
                else:
                    total_losses += 1
                    lose_rolls[(dice1, dice2)] += 1

            profit = g.balance - g.start_balance
            profits.append(profit)
        total_games = total_losses + total_wins
        avg_profit = sum(profits) / total_games
        win_rate = total_wins / total_games if total_games > 0 else 0

        most_common_win_roll = win_rolls.most_common(1)
        most_common_lose_roll = lose_rolls.most_common(1)

        return {
            "total_wins": total_wins,
            "total_losses": total_losses,
            "win_rate": win_rate,
            "avg_profit": avg_profit,
            "most_common_win_roll": most_common_win_roll,
            "most_common_lose_roll": most_common_lose_roll
        }
