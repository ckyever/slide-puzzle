import slidepuzzle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/api/puzzle", methods=['POST'])
def receivePuzzle():
    numbers = request.json
    print(numbers)
    moves = [slidepuzzle.Board.SLIDE_DOWN, slidepuzzle.Board.SLIDE_RIGHT, slidepuzzle.Board.SLIDE_UP, slidepuzzle.Board.SLIDE_LEFT]

    return jsonify(
        {
            "moves": moves
        }
    ), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)