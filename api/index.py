import json
from os.path import join
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

with open(join("data", "marks.json"), "r") as file:
    datas = json.load(file)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query = parse_qs(parsed_url.query)
        names = query["name"]

        ans = []

        for name in names:
            for data in datas:
                if name == data["name"]:
                    ans.append(data["marks"])


        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Allow-Headers", "Content-type")
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps({"marks": ans}).encode("utf-8"))
        return
