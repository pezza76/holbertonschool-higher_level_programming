from http.server import HTTPServer, BaseHTTPRequestHandler

# Step 1: Create your own handler
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Step 2: Tell the browser "Everything is OK"
        self.send_response(200)

        # Step 3: Tell the browser what kind of content you're sending
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Step 4: Send the actual message!
        message = "<html><body><h1>Hello, friend!</h1></body></html>"
        self.wfile.write(message.encode('utf-8'))

# Step 5: Set up and start the server
port = 8000
server = HTTPServer(('localhost', port), MyHandler)

print(f"Server running at http://localhost:{port}")
server.serve_forever()
