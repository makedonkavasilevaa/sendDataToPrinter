# echo-client.py

import socket

HOST = "10.10.21.31"  # The server's hostname or IP address
PORT = 6666  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected ")

    s.send(bytes.fromhex('02 36 32 33 35 30 36 33 35 7C 30 31 30 7C 7C 31 32 7C 7C 7C 7C 7C 7C 7C 03 0A'))

    print(f"Sent command ")
    data = s.recv(1024)
    print(f"Waiting response ")

print(f"Received {data!r}")

key_pressed = input('Press ENTER to continue: ')