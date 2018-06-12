import select
from socket import socket, AF_INET, SOCK_STREAM
import json
import time
from test_scripts import messages as msg

class Server:

    def __init__(self, address, port, num_of_clients, timeout):
        self.address = address
        self.port = port
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((self.address, self.port))
        self.sock.listen(num_of_clients)
        self.sock.settimeout(timeout)
        self.clients = []
        while True:
            try:
                conn, addr = self.sock.accept()
            except OSError as e:
                pass
            else:
                print('Client appended')
                self.clients.append(conn)
                print(self.clients)
            finally:
                self.r = []
                self.w = []
                self.e = []
                # print(self.r, self.w)
                try:
                    self.r, self.w, self.e = select.select(self.clients, self.clients, self.clients, 0)
                except:
                    pass
            # print('ww')
            self.send_probe(self.clients)


    def send_probe(self, w_clients):
        for client in w_clients:
            probe_msg = msg.JIMMessage()
            client.send(probe_msg.probe())



s = Server('localhost', 8886, 100, 0.2)

