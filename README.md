# CasinoGame

A console-based Python mini-game that simulates a simple casino dice game. Built with object-oriented principles and modular architecture, this project demonstrates core programming skills suitable for entry-level backend development.

## Features

- Dice rolling with betting system
- Tracks player balance
- Records history of game rounds
- Analyzes outcomes (wins, losses, draws)
- Automatically ends game when balance is too low
- Modular file structure (separated logic, UI, and statistics)

## Tech Stack

- **Python 3**
- Built-in modules: `random`, `collections`
- Object-Oriented Programming
- Command-line interface

## Sample Output

You rolled: 3 and 5
You lose $10.
Current balance: $90

Game history:
Rolled 3 and 5 - lost $10 | ...

Game results: {'lose': 1}

## Potential Improvements

- Add persistent storage (save/load game state)
- Improve randomness with weighted probabilities
- Add difficulty levels or betting multipliers
- Build a web-based version using Flask or Django
- Implement unit tests using `pytest`
- Add player profiles and stats history


## How to Run

```bash
git clone https://github.com/katebabakova444/CasinoGame.git
cd CasinoGame
python3 src/main.py

## Author
Kateryna Babakova