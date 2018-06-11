from socket import *
import json
import sys


s = socket(AF_INET, SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))


def make_pres_msg():
    pres_msg = {
        'action': 'presence',
        'type': 'online'
    }
    return pres_msg


def msg_encode(msg):
    j_msg = json.dumps(msg)
    b_msg = j_msg.encode('utf-8')
    return b_msg


def msg_decode(msg):
    b_msg = msg.decode('utf-8')
    j_msg = json.loads(b_msg)
    return j_msg


def send_msg(msg):
    s.send(msg_encode(msg))
    return None


def recv_msg():
    response = s.recv(1024)
    msg = msg_decode(response).get('text')
    print(msg)
    return msg


if __name__ == '__main__':

    msg = make_pres_msg()
    send_msg(msg)
    recv_msg()

    s.close()
