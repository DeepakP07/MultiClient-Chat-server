CS7NS1 (Scablable Computing) -- Assignment 1 (Chat Server)Multiple chat room with Multiple client.
========================================
***Student ID:17310212 Name: Deepak Purohit

Run start.sh to start the chat service

The ServerHostname/IP of the Instance is 127.0.0.1

The port Number is given as an argument in start.sh file

Server.py contains the code required for the server

Testing was not successful as the running the test with docker or opennebula gave connection error,
below sample output of the file is given.

### How to use:
* Download and unzip all the files. You'll also need Python 3 installed.
* To run server: 

***"host"(optional) is the ip address your server is running on. 

python3 pychat_server.py [host]


***To run client: "host"(not optional) should be the same ip address as the server

python3 pychat_client.py host
 
 ***After running server file output would be something like this :
  
  Last login: Thu Nov 23 15:00:38 on ttys002

python3 server.py 127.0.0.1 22223
Server Connected   ('127.0.0.1', 22223) 127.0.0.1
new says: name: deepak

Now listening at  ('127.0.0.1', 22223)
new says: name: maxjunior

New connection from: maxjunior

New connection from: deepak
deepak says: list .                        # To show all rooms available.

deepak says: join room1                    # To create and join room1

New connection from: sid
sid says: list

sid says: join room1

***After running Client file, the output would be something like this.

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
> Sid
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
room1 welcomes: Sid
> hey guys
Now listening at client
Now listening at client
Deepa:hey guys
> Now listening at client
deepak:hey pandian
> Now listening at client
sid: Later fellows. 
> quit    
Now listening at client
Now listening at client
Bye
