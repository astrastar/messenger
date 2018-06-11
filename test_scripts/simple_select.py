import select
from socket import socket, AF_INET, SOCK_STREAM
import json

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


def write_msg(requests, w_clients):
    for w in w_clients:
        if w in requests:
            try:
                # msg = 'hello'
                # j_msg = json.dumps(msg)
                # b_msg = j_msg.encode('utf-8')
                resp = requests[w].encode('ascii')
                w.send(resp)
            except:
                pass


def main():

    while True:
        try:
            conn, addr = s.accept()
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

        requests = read_msg(r)
        write_msg(requests, w)


main()



