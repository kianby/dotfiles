#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer


def build_json_message(message):
    response = {
        "message": message
    }
    return json.dumps(response).encode('utf-8')


class S(BaseHTTPRequestHandler):
    def _build_ok_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        logging.info("\nGET %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._build_ok_response()
        self.wfile.write(build_json_message("GET request for " + self.path))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("\nPOST %s\nHeaders:\n%s\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))
        self._build_ok_response()

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("\nPUT %s\nHeaders:\n%s\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))
        self._build_ok_response()

    def do_DELETE(self):
        logging.info("DELETE %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._build_ok_response()

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    # fh = logging.FileHandler('/tmp/pyserver.log')
    # logging.getLogger().addHandler(fh)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd on port %s...\n', port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
