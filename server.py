import select, socket, sys, pdb
from chat_util import Hall, Room, Player
import chat_util

READ_BUFFER = 4096
Host=''
host = sys.argv[1] if len(sys.argv) >= 2 else ''
listen_sock = chat_util.create_socket(('127.0.0.1', chat_util.PORT))

hall = Hall()
connection_list = []
connection_list.append(listen_sock)

while True:
    # Player.fileno()
    read_players, write_players, error_sockets = select.select(connection_list, [], [])
    for player in read_players:
        print(player)
        print(listen_sock)
        if player is listen_sock: # new connection, player is a socket
            new_socket, add = player.accept()
            new_player = Player(new_socket)
            connection_list.append(new_player)
            hall.welcome_new(new_player)

        else: # new message
            msg = player.socket.recv(READ_BUFFER)
            if msg:
                msg = msg.decode().lower()
                hall.handle_msg(player, msg)
            else:
                player.socket.close()
                connection_list.remove(player)

    for sock in error_sockets: # close error sockets
        sock.close()
        connection_list.remove(sock)

