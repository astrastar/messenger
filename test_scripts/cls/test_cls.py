import json
import time
from socket import *


class JIMMessage:

    msg = {
        'action': '',
        'time': time.ctime()
    }

    def encode(self, out_msg):
        j_msg = json.dumps(out_msg)
        b_msg = j_msg.encode('ascii')
        return b_msg

    def presence(self, acc_name, status):
        pres_msg = self.msg
        pres_msg['action'] = 'presence'
        pres_msg.update({'user': {
            'account_name': acc_name,
            'status': status
        }})
        return self.encode(pres_msg)

    def probe(self):
        probe_msg = self.msg
        probe_msg['action'] = 'probe'
        return self.encode(probe_msg)

    def auth(self, acc_name, pswrd):
        auth_msg = self.msg
        auth_msg['action'] = 'authenticate'
        auth_msg.update({'user': {
            'account_name': acc_name,
            'password': pswrd
        }})
        return self.encode(auth_msg)

    def clear(self):
        self.msg = {
            'action': '',
            'time': time.ctime()
        }

    def txt_msg(self, acc_name, text):
        txt_msg = self.msg
        txt_msg['action'] = 'text'
        txt_msg.update({
            'user': acc_name,
            'text:': text
        })
        return self.encode(txt_msg)

    def decode(self, inbox_msg):
        b_msg = inbox_msg.decode('ascii')
        j_msg = json.loads(b_msg)
        return j_msg



class JIMResponse:

    pass


class Client:

    def __init__(self, address, port, acc_name, pswrd):
        self.address = address
        self.port = port
        self.acc_name = acc_name
        self.pswrd = pswrd
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((self.address, self.port))

    def send_pres_msg(self, msg):
        self.sock.send(msg)

    def read_resp(self):
        response = self.sock.recv(1024)
        return response




if __name__ == '__main__':

    c = Client('localhost', 8886, 'dd', '324')
    msg = JIMMessage()
    # pres = msg.presence('max', 'online')
    # c.send_pres_msg(pres)
    # print(msg.decode(c.read_resp()))
    # msg.clear()
    # c.send_pres_msg(msg.txt_msg('max', 'hello!'))
    print(msg.decode(c.read_resp()))
    b = Client('localhost', 8886, 'dd', '324')
    print(msg.decode(b.read_resp()))