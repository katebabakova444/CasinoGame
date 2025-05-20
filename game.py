import random
from collections import Counter, defaultdict

class Game:
    def __init__(self, balance=100):
        self.balance = balance
        self.history = []
        self.outcomes = []
        self.roll_groups = defaultdict(list)
        self.total_won = 0
        self.total_lost = 0
        self.wins = 0
        self.losses = 0

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def play_round(self, bet):
        if bet < 5 or bet > self.balance:
            return {"status": "error", "message": "Invalid bet."}

        die1, die2 = self.roll_dice()
        if die1 == die2:
            outcome = "win"
            self.balance += bet * 2
            self.total_won += bet * 2
            self.wins += 1
        else:
            outcome = "lose"
            self.balance -= bet
            self.total_lost += bet
            self.losses += 1

        self.history.append((die1, die2))
        self.outcomes.append(outcome)
        self.roll_groups[outcome].append((die1, die2))

        return {
            "status": "ok",
            "outcome": outcome,
            "dice": (die1, die2),
            "balance": self.balance
        }