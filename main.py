from game.game import Game
from statistics import Statistics
from ui import UI

def main():
    game = Game()
    stats = Statistics()
    ui = UI()

    while True:
        choice = ui.get_user_choice()
        if choice == 'q':
            ui.display_history(game.history)
            ui.display_stats(stats.analyze(game.outcomes))
            break

        bet = ui.get_user_bet(game.balance)
        if bet is None:
            ui.display_message("Invalid input. Try again.")
            continue

        result = game.play_round(bet)

        if result["status"] == "ok":
            ui.display_result(result["outcome"], result["dice"], result["balance"])
        else:
            ui.display_message(result["message"])

        if game.balance < 5:
            ui.display_message("Game over! You're out of money.")
            ui.display_history(game.history)
            ui.display_stats(stats.analyze(game.outcomes))
            break

if __name__ == "__main__":
    main()