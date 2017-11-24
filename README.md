Multiple chat room with Multiple client.
======


### How to use:
* Download and unzip all the files. You'll also need Python 3 installed.
* To run server: 

"host"(optional) is the ip address your server is running on. 

python3 pychat_server.py [host]


* To run client: "host"(not optional) should be the same ip address as the server

python3 pychat_client.py host
 
 After running server file output would be something like this :
  
  Last login: Thu Nov 23 15:00:38 on ttys002

python3 server.py 127.0.0.1 22223
Server Connected   ('127.0.0.1', 22223) 127.0.0.1
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 22223)>
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 22223)>
<chat_util.Player object at 0x102a83dd8>
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 22223)>
new says: name: deepak

New connection from: deepak
<chat_util.Player object at 0x102a83dd8>
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 22223)>
deepak says: list

<chat_util.Player object at 0x102a83dd8>
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 22223)>
deepak says: join room1

New connection from: sid
<chat_util.Player object at 0x102c62ac8>
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 22223)>
sid says: list

<chat_util.Player object at 0x102c62ac8>
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 22223)>
sid says: join room1

After running Client file, the output would be something like this.

Last login: Fri Nov 24 10:19:07 on ttys003
python3 client.py 127.0.0.1 8888
Connected to server

Enter Helo to Continue.
  
 Helo
Helo Base_Test
IP Address is 10.6.55.236
8888
127.0.0.1
Student ID =17310212
Now listening at client
Welcome to chat.
Please tell us your name:
> Supreet
Now listening at client
Now listening at client
Instructions:
[list] to list all rooms
[join room_name] to join/create/switch to a room
[manual] to show instructions
[quit] to quit
Otherwise start typing and enjoy!
> list
Now listening at client
Now listening at client
Listing current rooms...
room1: 2 player(s)
> room1
Now listening at client
Now listening at client
You are currently not in any room! 
Use [list] to see available rooms! 
Use [join room_name] to join a room! 
> join room1
Now listening at client
Now listening at client
room1 welcomes: pandian
> hey guys
Now listening at client
Now listening at client
Supreet:hey guys
> Now listening at client
deepak:hey pandian
> Now listening at client
sid:hey 
> quit    
Now listening at client
Now listening at client
Bye
