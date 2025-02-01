from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=["POST"])
def update_seed():
    try:
        subprocess.Popen(["python3", "stress_cpu.py"]) 
        return "CPU stress initiated", 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def get_seed():
    private_ip = socket.gethostbyname(socket.gethostname())
    return f"Private IP: {private_ip}", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)