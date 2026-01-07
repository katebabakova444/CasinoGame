# Casino Game Simulator

**Backend Engineering Project (Python / Flask / Monte Carlo Simulation)**

Casino Game Simulator is a backend-focused Python project that models a casino betting game with both **CLI** and **REST API** interfaces.  
The project demonstrates backend architecture, testing, simulations, and statistical analysis, including **Monte Carlo simulations**.

The project started as a simple CLI betting game and evolved into a structured backend system with persistent storage, analytics, simulations, automated tests, and a deployed API.

Its main goal is to demonstrate backend engineering growth through clean architecture, separation of concerns, testing, and real-world probabilistic modeling.

---

## Project Goals

- Apply backend engineering principles to a probabilistic domain
- Practice clean architecture and separation of concerns
- Build and expose game logic via a REST API
- Implement Monte Carlo simulations for statistical analysis
- Design and test backend logic with unit and integration tests
- Support multiple interfaces (CLI and API)
- Show clear learning progression over project iterations

---

## What This Project Does

The Casino Game Simulator allows you to:

### CLI Mode
- Place bets and play individual game rounds
- Track balance changes during gameplay
- Run a lightweight interactive betting experience

> CLI mode is intentionally limited to gameplay only (no simulations or analytics) to keep responsibilities separated.

### API Mode
- Play the game
- Run Monte Carlo simulations
- Analyze game outcomes and statistics
- Persist game rounds and results
- Retrieve analytics and aggregated statistics
- Interact with the system as a backend service

---

## Architecture Overview 
``` text
CasinoGame/
├── game/
│   ├── init.py
│   ├── game.py          # Core game logic (bets, rounds, balance)
│   ├── analytics.py     # Game analytics and outcome aggregation
│   ├── statistics.py    # Statistical calculations
│   ├── simulation.py   # Monte Carlo simulation engine
│   ├── storage.py      # Persistence layer abstraction
│   ├── db.py           # Database logic
│   └── ui.py            # CLI interface
│
├── tests/
│   ├── test_game.py
│   ├── test_api.py
│   ├── test_analytics.py
│   ├── test_simulation.py
│   └── test_statistics.py
│
├── app.py               # Flask API entry point
├── main.py              # CLI entry point
├── requirements.txt
├── Procfile             # Deployment configuration
└── README.md
```


---

## Tech Stack

### Backend
- Python
- Flask
- SQLite
- pytest
- unittest.mock

### Concepts & Techniques
- Clean architecture
- Monte Carlo simulation
- Separation of CLI and API responsibilities
- Test isolation with mocks
- Persistent storage abstraction

---

## Core Features

- Game balance management
- Betting and round execution
- Outcome tracking
- Statistical analysis of results
- Monte Carlo simulations
- Persistent storage of rounds and games
- CLI gameplay interface
- REST API for full system access
- Deployed production-style backend service

---

## API Capabilities

Using the API, you can:

- Play game rounds
- Retrieve stored game data
- Run Monte Carlo simulations
- Analyze statistical outcomes
- Access aggregated analytics

> The API exposes functionality that is intentionally **not available in CLI mode**, reinforcing separation of concerns.

---

## Testing

All tests are written using **pytest**.

Test coverage includes:

### Unit Tests
- Game balance logic
- Betting mechanics
- Outcome tracking
- Statistics calculations
- Analytics aggregation

### Integration Tests
- API endpoints
- Storage interactions
- Simulation execution

Mocks (`unittest.mock`) are used to isolate dependencies such as storage and external interactions.

---

## Running Tests

```bash
python -m pytest
```

## Running Locally
CLI Mode
```bash
python main.py
```

API mode
```bash
python app.py
```

## Deployment

The API is deployed on Render as a production-style backend service:

**Live API:** https://casinogame-iica.onrender.com

---
## Author
Created by Kateryna Babakova (https://github.com/katebabakova444) This project is part of my backend development journey.