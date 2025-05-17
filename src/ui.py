from collections import Counter
import random
def play_round(self):
    try:
        min_bet = 5
        bet = int(input(f"Enter your bet (min: ${min_bet}, available: ${self.balance}): "))
        if bet < min_bet:
            print("Minimum bet is $5. Please enter a higher amount.")
            return
        if bet > self.balance or bet <= 0:
            print("Invalid bet amount.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    die1, die2 = self.roll_dice()
    print(f"You rolled: {die1} and {die2}")

def show_rolls_groups(self):
    print(f"Win rolls: {self.roll_groups['win']}")
    print(f"Lose rolls: {self.roll_groups['lose']}")

def roll_statistics(self):
    roll_counts = Counter(self.history)
    print("\n-- Dice Roll Frequencies --")
    for roll, count in roll_counts.items():
        print(f"{roll}: {count} times")

def print_summary(self):
    summary = self.analyze_outcome()
    print("\n--- Game Summary ---")
    print(f"Wins: {summary.get('win', 0)}")
    print(f"Loses: {summary.get('lose', 0)}")
    print(f"Final balance: ${self.balance}")