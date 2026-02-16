from flask import Flask, request, jsonify, send_from_directory
import magnitude_prob
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/<path:filename>")
def serve_static(filename):
    # This explicitly checks if the file exists before trying to serve it
    file_path = os.path.join(BASE_DIR, filename)
    if os.path.exists(file_path):
        return send_from_directory(BASE_DIR, filename)
    else:
        return f"File {filename} not found at {file_path}", 404

@app.route("/compute_prob")
def compute_prob():
    area = float(request.args.get("area", 1000))
    prob = magnitude_prob.compute_probability(area)
    return jsonify({"prob": prob})

if __name__ == "__main__":
    app.run(debug=True)
