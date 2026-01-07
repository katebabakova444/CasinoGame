import sqlite3
from game.db import get_db
conn = sqlite3.connect("casino.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS games (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     start_balance REAL,
     balance REAL,
     created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS rounds (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     game_id INTEGER,
     dice1 INTEGER,
     dice2 INTEGER,
     outcome TEXT,
     bet REAL,
     balance REAL,
     created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
conn.close()

class Storage:
    def start_game(self, start_balance):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO games (start_balance, balance)
            VALUES (?, ?)
            """,
            (start_balance, start_balance)
        )
        game_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return game_id
    def save_round(self, game_id, dice1, dice2, bet, outcome, balance):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO rounds (game_id, dice1, dice2, bet, outcome, balance)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (game_id, dice1, dice2, bet, outcome, balance)
        )
        conn.commit()
        conn.close()

    def finish_game(self, game_id, balance):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE games
            SET balance = ?
            WHERE id = ?
            """,
            (balance, game_id)
        )
        conn.commit()
        conn.close()
    def get_history(self, game_id):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT dice1, dice2, bet, outcome,balance, created_at
            FROM rounds
            WHERE game_id = ?
            ORDER BY created_at ASC
            """,
            (game_id,)
        )
        return cursor.fetchall()



