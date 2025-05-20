class UI:
    def get_user_choice(self):
        return input("\nPress Enter to play or 'q' to quit: ").lower()

    def get_user_bet(self, balance):
        try:
            bet = int(input(f"Enter your bet (min: $5, available: ${balance}): "))
            return bet
        except ValueError:
            print("Please enter a valid number.")
            return None

    def display_result(self, outcome, dice, balance):
        d1, d2 = dice
        print(f"\nYou rolled: {d1} and {d2}")
        if outcome == "win":
            print("You win!")
        else:
            print("You lose.")
        print(f"Current balance: ${balance}")

    def display_message(self, message):
        print(message)

    def display_history(self, history):
        print("\nGame history:")
        for roll in history:
            print(f"Rolled {roll[0]} and {roll[1]}")

    def display_stats(self, stats):
        print("\n--- Game Summary ---")
        print(f"Wins: {stats.get('win', 0)}")
        print(f"Losses: {stats.get('lose', 0)}")