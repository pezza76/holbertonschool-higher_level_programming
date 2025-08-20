from http.server import BaseHTTPRequestHandler, HTTPServer

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # Send "200 OK"
        self.send_header("Content-type", "text/plain")
        self.end_headers()  # End headers section
        self.wfile.write(b"Hello, this is a simple API!")  # Send response body

def run():
    server_address = ("", 8000)  # Listen on all interfaces at port 8000
    httpd = HTTPServer(server_address, myHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()






