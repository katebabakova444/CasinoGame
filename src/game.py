import random
from collections import Counter, defaultdict

class CasinoGame:
    def __init__(self, balance=100):
        self.balance = balance
        self.history = []
        self.total_won = 0
        self.total_lost = 0
        self.wins = 0
        self.losses = 0
        self.outcomes = []
        self.roll_groups = defaultdict(list)


    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

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

        if die1 == die2:
            outcome = "win"
            print(f"You win ${bet * 2}!")
            self.history.append(f"Rolled {die1} and {die2}")
            self.balance += bet * 2
            self.total_won += bet * 2
            self.wins += 1
            self.outcomes.append(outcome)
            self.roll_groups[outcome].append((die1, die2))
        else:
            outcome = "lose"
            print(f"You lose {bet}.")
            self.history.append(f"Rolled {die1} and {die2} - lost ${bet}")
            self.balance -= bet
            self.total_lost += bet
            self.losses += 1
            self.outcomes.append(outcome)
            self.roll_groups[outcome].append((die1, die2))
        print(f"Current balance: ${self.balance}")
        self.history.append((die1, die2))

    def analyze_outcome(self):
        return dict(Counter(self.outcomes))

    def show_rolls_groups(self):
        from src.ui import show_rolls_groups
        show_rolls_groups(self.roll_groups)

    def roll_statistics(self):
        from src.ui import roll_statistics
        roll_statistics(self.roll_groups)

    def print_summary(self):
        from src.ui import print_summary
        print_summary(self)


