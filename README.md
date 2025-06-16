# 🎲 Dice Betting Simulator

A Python-based CLI game that lets users place bets, roll dice, and simulate win/loss outcomes based on basic probability.  
The game tracks balance, logs results, and displays real-time stats using clean modular design.

---

## 💡 Why I Built This

I wanted to go beyond static scripts and write a full interactive loop — something with memory, user feedback, and persistent session data.  
This project helped me break a CLI tool into reusable, testable modules with a clear game state.

---

## ✨ Features

- Balance and betting system
- Two-dice roll with win/loss logic
- CLI input validation and user feedback
- Real-time tracking of game history and outcomes
- Modular architecture: `game.py`, `statistics.py`, `ui.py`

---

## 🧠 Tech & Concepts

- Python 3.10+
- Standard Libraries: `random`, `collections.Counter`
- Project architecture (splitting logic/UI/statistics)
- Probability logic and game state
- CLI formatting for user interaction
- Future-ready for unit testing and scaling

---

## ▶️ How to Run

```bash
git clone https://github.com/katebabakova444/CasinoGame.git
cd CasinoGame
python main.py
```

### Project Structure

CasinoGame/
├── main.py            # Entry point
├── game.py            # Core logic and dice mechanics
├── statistics.py      # Win/loss tracking
├── ui.py              # CLI interface
└── README.md


---

## Example Output

```bash
Press Enter to play or 'q' to quit:
Enter your bet (min: $5, available: $100): 20
You rolled: 3 and 6
You lose 20.
Current balance: $80

Press Enter to play or 'q' to quit: q

Game history:
Rolled 3 and 6

--- Game Summary ---
Wins: 3
Losses: 1
```

---

## 📚 What I Practiced
- Structuring a multi-file Python project
- Managing interactive game state and loops
- Simulating randomness and statistical outcomes
- Using Counter() to persist and analyze data
- Practicing clean code: readable, modular, reusable

## 👩‍💻 Author

Created by Kateryna Babakova (https://github.com/katebabakova444)
This project is part of my backend development journey.
View my full portfolio: kateryna-portfolio (https://github.com/katebabakova444/kateryna-portfolio)