import os
import socket

import time

PORT = int(8081)

sock = socket.socket()

sock.bind(("0.0.0.0", PORT))

sock.listen(5)

print("server is running on port %d*", PORT)

while True:
    client, addr = sock.accept()
    print("Accepted connection: {}".format(addr))

    while 1:
        message = input("Enter a message: ")

        client.send(bytes(message, 'utf-8'))
        print(client.recv(1024))