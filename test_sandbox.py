from game.game import Game
from statistics import Statistics
from analytics import GameAnalytics
g = Game(balance=100)
stats = Statistics()
analytics = GameAnalytics()
print("Round 1:", g.play_round(10))
print("Round 2:", g.play_round(20))
print("Round 3:", g.play_round(5))

print(g.outcomes)
print(stats.analyze_basic(g.outcomes))
result = analytics.analyze_rolls(g.history, g.roll_groups)
print("Roll groups: ", g.roll_groups)
print("Analytics: ", result)

