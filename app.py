from flask import Flask, request, jsonify
from game.game import Game
from game.statistics import Statistics
from game.analytics import GameAnalytics
from game.simulation import MonteCarloSimulator
from game.storage import Storage

app = Flask(__name__)

stats = Statistics()
storage = Storage()
game_id = storage.start_game(100)
analytics = GameAnalytics()
simulator = MonteCarloSimulator()
game = Game(balance=100, game_id=game_id, storage=storage)

@app.route("/play", methods=["POST"])
def play_round():
    data = request.get_json()
    bet = data.get("bet")

    if bet is None:
        return jsonify({"error": "Bet is required"}), 400

    result = game.play_round(bet)

    if game.balance < 5:
        storage.finish_game(game.game_id, game.balance)

    return jsonify(result), 200

@app.route("/history", methods=["GET"])
def history():
    return jsonify({"history": game.history}), 200

@app.route("/stats", methods=["GET"])
def stats_basic():
    result = stats.analyze_basic(game.outcomes)
    return jsonify(result), 200

@app.route("/predict", methods=["GET"])
def predict_balance():
    num_future_games = request.args.get("games", "50")
    num_future_games = int(num_future_games)
    result = analytics.predict_balance(game, game.history, num_future_games)
    return jsonify(result), 200

@app.route("/simulate", methods=["POST"])
def run_simulation():
    data = request.get_json()

    runs = data.get("runs", 1000)
    bet = data.get("bet", 5)
    rounds_per_run = data.get("rounds_per_run", 10)

    result = simulator.run_simulation(runs=runs, bet=bet, rounds_per_run=rounds_per_run)
    return jsonify(result), 200

@app.route("/history/db", methods=["GET"])
def history_db():
    history = storage.get_history(game.game_id)
    return jsonify({"history": history}), 200

@app.route("/")
def index():
    return jsonify({"message": "Casino Game API is running"}), 200

if __name__=="__main__":
    app.run(host="0.0.0.0", port=4550)
