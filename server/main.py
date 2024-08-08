import slidepuzzle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

puzzle = slidepuzzle.Board(4)
puzzle.scramble()

@app.route("/api/puzzle/new", methods=['POST'])
def newPuzzle():
    puzzle.scramble()

    return jsonify(
        {
            "message": "Puzzle was scrambled"
        }
    ), 200

@app.route("/api/puzzle", methods=['GET'])
def sendPuzzle():

    return jsonify(
        {
            "puzzle": puzzle.getBoard(),
            "size": puzzle.getSize(),
            "solved": puzzle.isSolved()
        }
    )

@app.route("/api/puzzle", methods=['POST'])
def receivePuzzle():
    data = request.json
    move = data["move"]

    if move == puzzle.SLIDE_UP:
        puzzle.slideUp()
    elif move == puzzle.SLIDE_RIGHT:
        puzzle.slideRight()
    elif move == puzzle.SLIDE_DOWN:
        puzzle.slideDown()
    elif move == puzzle.SLIDE_LEFT:
        puzzle.slideLeft()

    return jsonify(
        {
            "message": "Data received successfully",
            "received": data
        }
    ), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)