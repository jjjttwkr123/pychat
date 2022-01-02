# SocketChat v0.0.2

import socket
import threading

hostport = ('127.0.0.1', 9999)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(hostport)
true = True
print("TX-IP>", hostport)
def receve(s):
    global true
    while true:
        data = s.recv(1024).decode('utf8')
        if data == 'quit':
            true = False
        print("break. ")
        print('RX>', data)
        print("TX|")
        print("  V")
thrd=threading.Thread(target=receve,args=(s,))
thrd.start()
while true:
    user_input = input('TX>')
    s.send(user_input.encode('utf8'))
    if user_input == 'quit':
        true = False
s.close()