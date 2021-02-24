import socket
import sys
import time

PORT = 8081

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", PORT))
while True:
    message = client.recv(1024)
    print(message)
    message  = input("Send a message: ")
    
    client.send(bytes(message, 'utf-8'))