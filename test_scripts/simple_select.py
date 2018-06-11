import time
import select
from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8885))
s.listen(100)
s.settimeout(0.2)

clients = []


def read_msg(requests):
    responses = {}
    for req in requests:
        try:
            msg = req.recv(1024).decode('ascii')
            responses[req] = msg
            # print(msg)
        except:
            pass

    return responses


def write_msg():
    pass


def main():

    while True:
        try:
            # print('New request')
            conn, addr = s.accept()
            # clients.append(conn)
        except OSError as e:
            pass
        else:
            print('Client appended')
            clients.append(conn)
        finally:
            # print('3')
            r = []
            w = []
            try:

                r, w, e = select.select(clients, clients, clients, 0)

            except:
                pass

        # requests = r
        # print(requests)
        read_msg(r)
        # print(read_msg(requests))
        # print('writing: ', r)


main()



