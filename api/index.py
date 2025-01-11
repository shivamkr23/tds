# /api/index.py

import json
from os.path import join

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api")
def api():
    query = request.args.getlist("name")
    with open(join("data", "marks.json"), "r") as file:
        data = json.load(file)

    ans = []
    for d in data:
        if d["name"] in query:
            ans.append(d["marks"])

    return jsonify({"marks": ans}), 200
