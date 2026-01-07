from unittest.mock import Mock
from game.simulation import MonteCarloSimulator

def test_simulation_runs():
    mock_storage = Mock()

    sim = MonteCarloSimulator(storage=mock_storage)
    result = sim.run_simulation(runs=10, bet=5, rounds_per_run=5)

    assert "total_wins" in result
    assert "win_rate" in result
    assert "avg_profit" in result