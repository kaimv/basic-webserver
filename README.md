# Information

Hello! Thanks for coming to view this repoistory! It is currently under heavy development so please, expect bugs.

Curent bugs (Tick means bug is fixed):
- [ ] CTRL + C Does not end the program
- [ ] Random line added to text based responses

# Documentation

Welcome to the documentation. Below you will find a few examples of how to use the app and an explanation on what each function does.

### Basic setup

```python
import webserver

server = webserver.Server(host = '0.0.0.0', port = 80)

@server.route('/')
def index(request, response):
    return 200, "Hello world!"

server.start()
```

Explaination:

`import webserver` imports the module into the file so we can access it within itself.

`server = webserver.Server(host = '0.0.0.0', port = 80)` calls the Server class from the module which starts a HTTP server on 0.0.0.0 (All addresses) on port 80.

`@server.route('/')` sets a new accessable path over the address and port.

`def index(request, response):` the function that allows the server to respond with a status code and a text/template based content.

`return 200, "Hello world!"` returns the status code "200" which means OK request with the text content "Hello world!".

`server.start()` starts the server on the address and port specified in the `Server()` class.
