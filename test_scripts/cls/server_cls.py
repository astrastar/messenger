import select
from socket import socket, AF_INET, SOCK_STREAM
import json
import time
from test_scripts import client_copy

class Server:

    def __init__(self, address, port, num_of_clients, timeout):
        self.addres = address
        self.port = port
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((self.addres, self.port))
        sock.listen(num_of_clients)
        sock.settimeout(timeout)