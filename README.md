# Dice Betting Simulator

**Dice Betting Simulator** is a Python-based CLI game that allows users to place bets, roll two dice, and simulate win/loss outcomes based on basic betting logic.  
The game tracks balance, logs results, and displays statistics in real-time.

---

## Features

- User balance and bet system
- Two-dice roll with win/loss conditions
- Input validation and CLI interaction
- Real-time game history and statistics
- Modular structure (`game.py`, `statistics.py`, `ui.py`)

---

## Tech Stack

- Python 3.10+
- `random` — for dice rolls
- `collections.Counter` — to analyze win/loss outcomes
- CLI input/output

---

### Installation

git clone https://github.com/katebabakova444/CasinoGame.git
cd CasinoGame
python main.py

---

### Project Structure

CasinoGame/
├── main.py            # Entry point
├── game.py            # Core logic and dice mechanics
├── statistics.py      # Win/loss tracking
├── ui.py              # CLI interface
└── README.md

---


## What I Learned

- How to structure a Python project into multiple logical modules
- Writing a basic CLI game loop with user input and validation
- Simulating probability using `random` and interpreting results
- Using `collections.Counter` for tracking statistics
- Managing game state (balance, history, outcomes) across sessions
- Practicing clean, readable, and reusable Python code

---

## Author

**Kateryna Babakova**  
Self-taught backend developer with a background in anesthesiology  
Participant of DPI Cohort (May 2025)  
Actively preparing for Microsoft Leap and Google Apprenticeship  
[GitHub Profile](https://github.com/katebabakova444)

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

---
*Project built for learning and portfolio purposes.*