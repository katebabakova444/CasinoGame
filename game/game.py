import random
MIN_BET = 5
WIN_MULTIPLAYER = 2
class Game:
    def __init__(self,balance=100, game_id=None, storage=None):
        self.start_balance = balance
        self.balance = balance
        self.game_id = game_id
        self.storage = storage
        self.history = []
        self.outcomes = []
        self.roll_groups = {"win": [], "lose": []}
        self.total_wins = 0
        self.total_losses = 0

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def validate_bet(self, bet):
        if not isinstance(bet, int):
            return False, "Bet must be an integer."
        if bet < MIN_BET:
            return False, f"Minimum bet is ${MIN_BET}."
        if bet > self.balance:
            return False, "Bet exceeds current balance."

        return True, None

    def play_round(self, bet):
        is_valid, error_message = self.validate_bet(bet)
        if not is_valid:
            return {
                "status": "error",
                "message": error_message,
                "balance": self.balance
            }

        dice1, dice2 = self.roll_dice()
        self.history.append((dice1, dice2))

        if dice1 == dice2:
            outcome = "win"
            self.balance += bet * WIN_MULTIPLAYER
            self.total_wins += 1
        else:
            outcome = "lose"
            self.balance -= bet
            self.total_losses += 1
        self.outcomes.append(outcome)
        self.roll_groups[outcome].append((dice1, dice2))
        self.storage.save_round(
            self.game_id,
            dice1,
            dice2,
            bet,
            outcome,
            self.balance
        )
        return {
            "status": "ok",
            "outcome": outcome,
            "dice": (dice1, dice2),
            "balance": self.balance,
            "bet": bet

        }