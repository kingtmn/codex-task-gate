from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time

ITEMS = [{"id": i, "name": f"item-{i}"} for i in range(50)]
PAGE = b"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Mini site</title>
    <style>button { padding: 8px 12px; }</style>
  </head>
  <body>
    <button>Click me</button>
    <p>Helo world</p>
  </body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(PAGE)
            return
        if self.path == "/api/items":
            time.sleep(1.2)
            payload = json.dumps(ITEMS).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(payload)
            return
        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
