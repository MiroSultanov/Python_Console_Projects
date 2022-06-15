import socket

hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)

print(f'My IP Address is: {IPAddress}')