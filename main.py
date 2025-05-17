from src.game import CasinoGame
def main():
    game = CasinoGame()

    while True:
        choice = input("\nPress Enter to play or 'q' to quit: ")
        if choice.lower() == 'q':
            print("\nGame history:")
            print(" | ".join(str(outcome) for outcome in game.history))
            stats = game.analyze_outcome()
            print("Game results: ", stats)
            break
        game.play_round()
        if game.balance < 5:
            print("Game over! You're out of money.")
            print("\nGame history:")
            print(" | ".join(str(outcome) for outcome in game.history))
            stats = game.analyze_outcome()
            print("Game results: ", stats)
            break

if __name__ == "__main__":
    main()
