import basic_webserver

server = basic_webserver.Server(host='0.0.0.0', port=80)

@server.route('/', rate_limit=5, rate_limit_expire=5, methods=['POST'])
def index(request, response):
    if request.method == 'POST':
        print(request.body)
        return 200, 'Sent data to server.'

server.start()
