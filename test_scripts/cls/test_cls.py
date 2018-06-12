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
        self.msg['action'] = 'presence'
        self.msg.update({'user': {
            'account_name': acc_name,
            'status': status
        }})

    def probe(self):
        self.msg['action'] = 'probe'

    def auth(self, acc_name, pswrd):
        self.msg['action'] = 'authenticate'
        self.msg.update({'user': {
            'account_name': acc_name,
            'password': pswrd
        }})

    def clear(self):
        self.msg = {
            'action': '',
            'time': time.ctime()
        }

    def txt_msg(self, acc_name, text):
        self.msg['action'] = 'text'
        self.msg.update({
            'user': acc_name,
            'text:': text
        })

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


c = Client('localhost', 8885, 'dd', '324')
msg = JIMMessage()
pres = msg.presence('max', 'online')

c.send_pres_msg(msg.presence('max', 'online').encode())
print(msg.decode(c.read_resp()))