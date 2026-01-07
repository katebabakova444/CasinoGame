from unittest.mock import Mock,ANY
from game.game import Game

def test_game_balance():
    game = Game(balance=100)
    assert game.balance == 100

def test_play_round():
    mock_storage = Mock()
    game = Game(balance=100, storage=mock_storage)

    game.play_round(5)

    mock_storage.save_round.assert_called_once_with(
        ANY,
        ANY,
        ANY,
        5,
        ANY,
        ANY
    )

def test_play_round_updates_outcomes():
    mock_storage = Mock()
    game = Game(balance=100, storage=mock_storage)
    game.play_round(5)
    assert len(game.outcomes) == 1
