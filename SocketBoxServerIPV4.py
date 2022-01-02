import socket
import threading                       
print("Waitting to be connected......")
HostPort = ('0.0.0.0',9999)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)            
s.bind(HostPort)
s.listen(1)
conn,addr = s.accept()
true=True
addr = str(addr)
print('TX-IP> %s ' %addr )
print("RX-IP>",HostPort)
def Receve(conn):                                               
    global true                                                 
    while true:
        data = conn.recv(1024).decode('utf8')          
        if data == 'quit':
            true=False
        print("break. ")
        print("SRX> "+data+" from"+addr)                        
        print("STX>")
thrd=threading.Thread(target=Receve,args=(conn,))               
thrd.start()
while true:
    user_input = input('STX>')
    conn.send(user_input.encode('utf8'))                        
    if user_input == 'quit':                                    
        true = False
    #conn.close()
s.close()
print("SMSG> Disconnect...")
