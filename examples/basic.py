# Import the webserver module
import webserver

# Create a server instance with host '0.0.0.0' and port 80
server = webserver.Server(host='0.0.0.0', port=80)

# Define a route for the root URL '/'
@server.route('/')
# Define a function to handle requests to the root URL
def index(request, response):
    # Return a tuple containing the HTTP status code 200 and the message "Hello world!"
    return 200, "Hello world!"

# Start the server
server.start()
