"""
the client of sending any text
"""

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 8080

client.connect((host, port))


while True:
    send_msg = input("sending: ")

    if send_msg == "q":
        break
    send_msg = send_msg

    client.send(send_msg.encode("utf-8"))

    msg = client.recv(1024)


client.close()
