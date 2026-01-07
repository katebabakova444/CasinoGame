from unittest.mock import Mock
from game.game import Game
from game.analytics import GameAnalytics

def test_analyze_rolls_returns_dict():
    mock_storage = Mock()
    game = Game(balance=100, storage=mock_storage)
    game.play_round(5)

    analytics = GameAnalytics()
    result = analytics.analyze_rolls(game, game.history, game.roll_groups)

    assert isinstance(result, dict)
    mock_storage.save_round.assert_called()

def test_analyze_rolls_empty_game():
    game = Game(balance=100, storage = Mock())

    analytics = GameAnalytics()
    result = analytics.analyze_rolls(game, game.history, game.roll_groups)

    assert isinstance(result, dict)