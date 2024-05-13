# Import the webserver module
import webserver

# Create an instance of the Server class with host address '0.0.0.0' and port number 80
server = webserver.Server(host='0.0.0.0', port=80)

# Decorator to register a function to be called before each request
@server.before_request
def before(request):
    # Print information about the incoming request: Client's IP address, requested path, and request method
    print(f'{request.client_address[0]} - {request.path} [{request.method}]')

# Define a function to handle requests to the root URL
@server.route('/')
def index(request, response):
    # This function returns a tuple with HTTP status code 200 and a message "Hello world!"
    return 200, "Hello world!"

# Start the server
server.start()
