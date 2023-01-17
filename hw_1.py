from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = 'localhost'
server_port = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        result_string = 'Hello, World wide web!'

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(result_string, "utf-8"))


if __name__ == '__main__':
    web_server = HTTPServer((hostname, server_port), MyServer)
    print('Server started http://%s:%s' % (hostname, server_port))
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    web_server.server_close()
    print('Server stopped.')
