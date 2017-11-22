import select, socket, sys
from chat_util import Room, Hall, Player
import chat_util
READ_BUFFER = 4096

host = '127.0.0.1'
port = '22223'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

if len(sys.argv) < 2:
    print("Usage: Python client.py [host]", file = sys.stderr)
    sys.exit(1)
else:
    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_connection.connect((sys.argv[1], chat_util.PORT))

def prompt():
    print('>', end=' ', flush = True)
    

print("Connected to server\n")
msg_prefix = ' '

Helo = input(" ")
print(Helo)
print("IP Address is" ' ' + s.getsockname()[0])
print(port)
print (host)
print ("Student ID =17310212")
     
socket_list = [sys.stdin, server_connection]
while True:
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [] ,[])
    for s in read_sockets:
        print("Now listening at client")
        if s is server_connection: # incoming message 
            msg = s.recv(READ_BUFFER)
            if not msg:
                print("Server down!")
                sys.exit(2)
            else:
                if msg == chat_util.QUIT_STRING.encode():
                    sys.stdout.write('Bye\n')
                    sys.exit(2)
                else:
                    sys.stdout.write(msg.decode())
                    if 'Please tell us your name' in msg.decode():
                        msg_prefix = 'name: ' # identifier for name
                    
                        
                    else:
                        msg_prefix = ''
                    prompt()

        else:
            msg = msg_prefix + sys.stdin.readline()
            server_connection.sendall(msg.encode())


