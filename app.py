from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/plain; charset=utf-8")
		self.end_headers()
		self.wfile.write(b"Hello world")


server = HTTPServer(("0.0.0.0", 32777), HelloHandler)

print("Server started on port 32777")
server.serve_forever()
