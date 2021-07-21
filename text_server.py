"""
the server of receiving any text
"""

import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8080

socket_server.bind((host, port))

socket_server.listen(5)
client_socket, address = socket_server.accept()

while True:
    print('start')
    recvmsg = client_socket.recv(1024)
    strData = recvmsg.decode("utf-8")
    if strData == 'q':
        break
    print("receive: %s" % strData)
    msg = input("send: ")
    client_socket.send(msg.encode("utf-8"))

socket_server.close()
