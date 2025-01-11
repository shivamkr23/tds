# /api/index.py

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Flask Vercel Example - Hello World", 200

@app.route("/api", methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        return jsonify({"marks": 100}), 200
    else:
        return jsonify({"marks": 0}), 200



@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

