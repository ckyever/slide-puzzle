import slidepuzzle
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/api/puzzle", methods=['GET'])
def puzzle():
    puzzle = slidepuzzle.Board(4)
    return jsonify(
        {
            "puzzle": puzzle.getBoard()
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)