import json
from http.server import BaseHTTPRequestHandler
from os.path import join
from urllib.parse import urlparse, parse_qs


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with open(join("data", "marks.json"), "r") as file:
            datas = json.load(file)

        parsed_url = urlparse(self.path)
        query = parse_qs(parsed_url.query)

        names = query.get("names")
        ans = []

        if isinstance(names, list):
            for data in datas:
                if data["name"] in names:
                    ans.append(data["marks"])

        elif names is not None:
            for data in datas:
                if data["name"] == names:
                    ans.append(data["marks"])

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps({"marks": ans}).encode("utf-8"))
        return
