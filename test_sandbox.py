from game.game import Game
from game.simulation import MonteCarloSimulator
from statistics import Statistics
from game.analytics import GameAnalytics

g = Game(balance=100)
stats = Statistics()
analytics = GameAnalytics()

print("Round 1:", g.play_round(5))
print("Round 2:", g.play_round(20))
print("Round 3:", g.play_round(5))

print(g.outcomes)
print(stats.analyze_basic(g.outcomes))

result = analytics.analyze_rolls(g, g.history, g.roll_groups)

print("Roll groups: ", g.roll_groups)
print("Analytics: ", result)

sim = MonteCarloSimulator()
print(sim.run_simulation(runs=1000, bet=5, rounds_per_run=10))

