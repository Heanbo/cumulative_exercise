# Import HTTP server and handler classes from Python's standard library.
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define some variables.
ip = "0.0.0.0"
port = 8080
server_address = (ip, port)

# Define and init a variable called "api" using the classes we imported.
api = HTTPServer(
    server_address=server_address, RequestHandlerClass=SimpleHTTPRequestHandler
)

# Start the HTTP server.
print("Listening for HTTP requests...")
api.serve_forever()
