import slidepuzzle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/api/puzzle", methods=['GET'])
def sendPuzzle():
    puzzle = slidepuzzle.Board(4)
    return jsonify(
        {
            "puzzle": puzzle.getBoard(),
            "size": puzzle.getSize()
        }
    )

@app.route("/api/puzzle", methods=['POST'])
def receivePuzzle():
    data = request.json
    print("This is Flask we received = ", data)
    return jsonify(
        {
            "message": "Data received successfully",
            "received": data
        }
    ), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)