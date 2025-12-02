from game.game import Game
from game.statistics import Statistics
from game.ui import UI
from game.storage import Storage

def main():
    game = Game()
    stats = Statistics()
    ui = UI()
    storage = Storage()

    while True:
        choice = ui.get_user_choice()

        if choice == 'q':
            ui.display_history(game.history)
            ui.display_stats(stats.analyze(game.outcomes))
            storage.save_game_session(game.history)
            break

        bet = ui.get_user_bet(game.balance)
        if bet is None:
            ui.display_message("Invalid input. Try again.")
            continue

        result = game.play_round(bet)

        if result["status"] == "ok":
            ui.display_result(
                result["outcome"],
                result["dice"],
                result["balance"])
        else:
            ui.display_message(result["message"])

        if game.balance < 5:
            ui.display_message("Game over! You're out of money.")
            ui.display_history(game.history)
            ui.display_stats(stats.analyze(game.outcomes))
            storage.save_game_session(game.history)
            storage.finish_game(game.game_id, game.balance)
            break

if __name__ == "__main__":
    main()