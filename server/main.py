from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/puzzle", methods=['GET'])
def puzzle():
    return jsonify(
        {
            "puzzle": "test"
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)