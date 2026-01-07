from game.statistics import Statistics


def test_statistics():
    outcomes = ["win", "lose", "win"]
    stats = Statistics()

    result = stats.analyze_basic(outcomes)

    assert result["wins"] == 2
    assert result["losses"] == 1
    assert result["total_games"] == 3

def test_statistics_empty_input():
    stats = Statistics()

    result = stats.analyze_basic([])

    assert result["wins"] == 0
    assert result["losses"] == 0
    assert result["total_games"] == 0
    assert result["win_rate"] == 0