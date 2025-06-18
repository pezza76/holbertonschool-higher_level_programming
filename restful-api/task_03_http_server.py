from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode())  # Send message as bytes

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode())  # Send message as bytes

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "OK"
            self.wfile.write(message.encode())  # Send message as bytes

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "Endpoint not found"
            self.wfile.write(message.encode())  # Send message as bytes

server_address = ('localhost', 8000)

httpd = HTTPServer(('localhost', 8000), MyHandler)

print("Server running on http://localhost:8000")
httpd.serve_forever()