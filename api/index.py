# /api/index.py

import json
from os.path import join

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Flask Vercel Example - Hello World", 200


@app.route("/api")
def api():
    query = request.args.getlist("name")
    with open(join("data", "marks.json"), "r") as file:
        data = json.load(file)

    ans = []
    for d in data:
        if d['name'] in query:
            ans.append(d['marks'])

    return jsonify({"marks": ans}), 200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

