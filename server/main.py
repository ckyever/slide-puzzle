import math
from flask import Flask, request, jsonify
from flask_cors import CORS
import slidepuzzle

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/api/puzzle", methods=['POST'])
def receivePuzzle():
    boardData = request.json
    sortedBoardData = sorted(boardData, key=lambda x: x['index'])
    puzzleArray = [tile['value'] for tile in sortedBoardData]
    size = int(math.sqrt(len(puzzleArray)))

    # Replace the empty tile with 0
    puzzleArray = [0 if tile == len(puzzleArray) else tile for tile in puzzleArray]

    # Creates 2D array by slicing the 1D array into rows
    twodPuzzleArray = [puzzleArray[row * size:(row+1) * size] for row in range(size)]

    # Create our representation of the board
    puzzle = slidepuzzle.Board(size)
    puzzle.setBoard(twodPuzzleArray)
    puzzle.printCurrentBoard()

    # CKYTODO: Get the moves
    moves = []

    return jsonify(
        {
            "moves": moves
        }
    ), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)