from flask import Flask, request, jsonify

app = Flask(__name__)

seed = 0

@app.route("/", methods=["POST"])
def update_seed():
    try:
        data = request.get_json()
        if data is None or "num" not in data:
             return jsonify({"error": "Missing or invalid JSON data.  Provide {'num': integer}"}), 400
        
        new_seed = data.get("num")
        if not isinstance(new_seed, int):
             return jsonify({"error": "'num' must be an integer"}), 400

        global seed
        seed = new_seed
        return "", 204

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def get_seed():
    global seed
    return str(seed), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)